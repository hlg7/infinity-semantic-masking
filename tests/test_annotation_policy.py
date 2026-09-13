import unittest,json
from annotation_policy import POLICY,system_prompt,decode_groups,validate_labels
from annotate_semantics import split_words

class AnnotationPolicyTests(unittest.TestCase):
    def test_shared_rules_and_brightness_normalization(self):
        prompt='A red cup is on a dark tiled table under soft daylight.'
        words=split_words(prompt);groups={s:[] for s in POLICY['labels']}
        for i,text,label in [(1,'red','color'),(2,'cup','object'),(4,'on','spatial_relation'),(6,'dark','color'),(7,'tiled','texture'),(8,'table','object'),(9,'under','spatial_relation')]:groups[label].append([i,text])
        labels=decode_groups(json.dumps(groups),words)
        record={'id':'p1','prompt':prompt,'target_semantic':'color'}
        labels,annotation,corrections=validate_labels(record,labels,{'spans':[[2,5]]})
        self.assertEqual([labels[i] for i in (6,7,9)],['other']*3)
        self.assertEqual(labels[1],'color');self.assertEqual(labels[2],'object')
        self.assertEqual(''.join(x['text'] for x in annotation['segments']),prompt)
        self.assertEqual(len(corrections),3)
        self.assertIn(json.dumps(POLICY),system_prompt())

    def test_repeated_words_and_bad_indices(self):
        words=split_words('A red cup beside a red plate.')
        groups={s:[] for s in POLICY['labels']};groups['color']=[[1,'red'],[5,'red']]
        self.assertEqual([i for i,x in enumerate(decode_groups(json.dumps(groups),words)) if x=='color'],[1,5])
        groups['object']=[[1,'red']]
        with self.assertRaises(ValueError):decode_groups(json.dumps(groups),words)
        groups['object']=[[2,'spoon']]
        with self.assertRaises(ValueError):decode_groups(json.dumps(groups),words)
        groups['object']=[[2,'plate']];repairs=[]
        self.assertEqual(decode_groups(json.dumps(groups),words,repairs)[6],'object')
        self.assertEqual(repairs,[{'text':'plate','model_index':2,'resolved_index':6}])
        groups['object']=[[2,'red']]
        with self.assertRaises(ValueError):decode_groups(json.dumps(groups),words)

    def test_missing_known_target_rejected(self):
        r={'id':'p','prompt':'A red cup.','target_semantic':'color'}
        with self.assertRaises(ValueError):validate_labels(r,['other']*4,{'spans':[[2,5]]})

if __name__=='__main__':unittest.main()
