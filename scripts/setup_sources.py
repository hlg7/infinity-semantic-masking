"""Fetch the pinned Infinity source and apply the shared baseline/mask patch."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = json.loads((ROOT/'vendor/sources.json').read_text())['Infinity']
    repo = ROOT/'vendor/Infinity'
    if not repo.exists():
        subprocess.run(['git','clone','--no-checkout',source['url'],str(repo)],check=True)
        subprocess.run(['git','-C',str(repo),'checkout','--detach',source['revision']],check=True)
    actual = subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
    if actual != source['revision']:
        raise RuntimeError('Existing Infinity checkout has a different revision; refusing to change it')
    patch = str(ROOT/'reports/infinity_scale_index.patch')
    base = ['git','-C',str(repo),'apply']
    if subprocess.run(base+['--reverse','--check',patch],capture_output=True).returncode == 0:
        print('Pinned Infinity source already has the scale_ind patch')
        return
    subprocess.run(base+['--check',patch],check=True)
    subprocess.run(base+[patch],check=True)
    print('Pinned Infinity source and scale_ind patch ready')


if __name__ == '__main__':
    main()
