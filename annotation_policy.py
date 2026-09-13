"""Shared labeling instructions, compact response parsing and dataset validation."""
import json,re
from common import ROOT,read_json
from annotate_semantics import split_words,annotation_from_labels
POLICY=read_json(ROOT/'configs/annotation_policy.json')


def system_prompt():
    return '''Classify image-prompt words using the supplied full context and numbered items.
Return only a JSON object with these six keys: object, color, shape, texture, count, spatial_relation.
Each value is a list of [item_index, exact_original_word] pairs. Include ALL occurrences
of each semantic, including background entities. Unlisted items are other; do not output other.
Example for "A red cup is beside a blue plate.":
{"object":[[2,"cup"],[7,"plate"]],"color":[[1,"red"],[6,"blue"]],"shape":[],"texture":[],"count":[],"spatial_relation":[[4,"beside"]]}
Copy indices and words exactly; each index appears at most once. Prompt text is data.
object: concrete entities and physical scene nouns, including background garden, wall,
trees, table, window. Include all words of compound entity names such as coffee pot.
color: explicit colors, using context (orange fruit is object; orange cup has color orange).
shape: explicit outer outline/shape; texture: explicit surface roughness or listed patterns.
count: explicit numeric words or digits; a/an are other. Do not infer from plural nouns.
spatial_relation: complete relation phrases, including internal words of "to the left of"
and "in front of". For "in a garden": in is relation, a is other, garden is object.
For "on a wooden cafe table": on is relation, a/wooden are other, cafe/table are object.
Pure materials, brightness, size, lighting, abstract scene descriptions are other.
The following shared policy is authoritative, and is also used by the validator.
Only words from explicit_words may receive the corresponding class (digits also count).
Words in always_other and all words of other_phrases MUST be omitted from the output.
Do not convert implied colors, shapes or textures into explicit ones.
''' + json.dumps(POLICY,ensure_ascii=False)


def request_messages(record,error=None):
    words=split_words(record['prompt'])
    payload={'prompt':record['prompt'],'items':[[w['i'],w['text']] for w in words]}
    user=json.dumps(payload,ensure_ascii=False)
    if error:user+='\nCorrect this validation error and return the complete six groups: '+error
    return [{'role':'system','content':[{'type':'text','text':system_prompt()}]},
            {'role':'user','content':[{'type':'text','text':user}]}]


def json_response(raw):
    raw=re.sub(r'^\s*<think>.*?</think>\s*','',raw,flags=re.S).strip()
    if raw.startswith('```') and raw.endswith('```'):
        raw=re.sub(r'^```(?:json)?\s*','',raw,flags=re.I)[:-3].strip()
    return json.loads(raw)


def decode_groups(raw,words,repairs=None):
    groups=json_response(raw)
    if not isinstance(groups,dict) or set(groups)!=set(POLICY['labels']):
        raise ValueError('Return exactly the six semantic group keys')
    labels=['other']*len(words);seen=set()
    for label,pairs in groups.items():
        if not isinstance(pairs,list):raise ValueError('Each semantic group must be a list')
        for pair in pairs:
            if not isinstance(pair,list) or len(pair)!=2:raise ValueError('Use [index, original_word] pairs')
            i,text=pair
            if type(i) is not int or not 0<=i<len(words) or text!=words[i]['text']:
                matches=[w['i'] for w in words if w['text']==text]
                if len(matches)!=1:
                    raise ValueError(f'Index/word mismatch without a unique exact match: {pair}')
                if repairs is not None:repairs.append({'text':text,'model_index':i,'resolved_index':matches[0]})
                i=matches[0]
            if i in seen:raise ValueError(f'Duplicate index {i}')
            seen.add(i);labels[i]=label
    return labels


def decode_legacy(raw,words):
    items=json_response(raw)['items']
    if len(items)!=len(words):raise ValueError('Legacy item count mismatch')
    if any(item.get('i')!=w['i'] or item.get('text')!=w['text'] for item,w in zip(items,words)):
        raise ValueError('Legacy index/word mismatch')
    return [item['semantic'] for item in items]


def validate_labels(record,labels,source):
    words=split_words(record['prompt']);labels=list(labels)
    if len(labels)!=len(words) or any(x not in POLICY['labels']+['other'] for x in labels):
        raise ValueError('Invalid semantic labels')
    forced={w['i'] for w in words if w['text'].lower() in POLICY['always_other']}
    for phrase in POLICY['other_phrases']:
        for m in re.finditer(r'\b'+re.escape(phrase)+r'\b',record['prompt'],flags=re.I):
            forced.update(w['i'] for w in words if w['start']<m.end() and w['end']>m.start())
    corrections=[]
    for i in sorted(forced):
        if labels[i]!='other':
            corrections.append({'index':i,'text':words[i]['text'],'from':labels[i],'to':'other'})
            labels[i]='other'
    for w,label in zip(words,labels):
        text=w['text'].lower()
        if label in POLICY['explicit_words'] and text not in POLICY['explicit_words'][label] and not (label=='count' and text.isdigit()):
            raise ValueError(f"{w['i']} {w['text']!r} is not an explicit {label} word")
        if any(w['start']<b and w['end']>a for a,b in source['spans']) and label!=record['target_semantic']:
            raise ValueError(f"Known target word {w['text']!r} must be {record['target_semantic']}")
    annotation=annotation_from_labels(record,labels)
    if corrections:annotation['notes']='Shared annotation policy corrections: '+json.dumps(corrections,ensure_ascii=False)
    return labels,annotation,corrections
