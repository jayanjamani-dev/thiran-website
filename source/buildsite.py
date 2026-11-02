import re,os,json,shutil,hashlib,sys
from PIL import Image
OUT=sys.argv[1]; t=open('v8.tpl.html').read()
A=os.path.join(OUT,'assets'); os.makedirs(A,exist_ok=True)
cache={}
def asset(p):
    if p in cache: return cache[p]
    if p.startswith(('data:','http','${','#','/')): return p
    rp=os.path.realpath(p); base=os.path.basename(p).replace('@1x','')
    stem,ext=os.path.splitext(base); h=hashlib.md5(open(rp,'rb').read()).hexdigest()[:8]
    if ext.lower()=='.jpg' or ext.lower()=='.jpeg':
        name=f'{stem}-{h}.jpg'; im=Image.open(rp).convert('RGB')
        if stem.startswith(('hero-lap3','hero-lap4')): shutil.copy(rp,os.path.join(A,name))
        else:
            if im.width>2400: im=im.resize((2400,round(im.height*2400/im.width)),Image.LANCZOS)
            im.save(os.path.join(A,name),quality=82,optimize=True,progressive=True)
    elif stem=='hero-full':
        name=f'{stem}-{h}.jpg'; Image.open(rp).convert('RGB').save(os.path.join(A,name),quality=93,subsampling=0,optimize=True,progressive=True)
    elif ext.lower()=='.png' and os.path.getsize(rp)>150000:
        name=f'{stem}-{h}.jpg'; Image.open(rp).convert('RGB').save(os.path.join(A,name),quality=86,optimize=True,progressive=True)
    else:
        name=f'{stem}-{h}{ext}'; shutil.copy(rp,os.path.join(A,name))
    cache[p]='assets/'+name; return cache[p]
PICK=[['text','callout','cloud','pen','highlighter','arrow','rectangle','dimension'],['length','polylength','area','count','volume','dynamicFill','visualSearch','lineTrace'],['stamp','signature','image','snapshot','photo','table','legend','tag'],['cloud','callout','note','approval','stamp','textHighlight','textUnderline','textStrikeout']]
N={'text':'Text box','callout':'Callout','cloud':'Cloud','pen':'Pen','highlighter':'Highlighter','arrow':'Arrow','rectangle':'Rectangle','dimension':'Dimension','length':'Length','polylength':'Run length','area':'Area','count':'Count','volume':'Volume','dynamicFill':'Fill Area','visualSearch':'Find Similar','lineTrace':'Service takeoff','stamp':'Stamp','signature':'Signature','image':'Image','snapshot':'Snapshot','photo':'Photo pin','table':'Schedule','legend':'Legend','tag':'Label','note':'Sticky note','approval':'Approval stamp','textHighlight':'Highlight text','textUnderline':'Underline','textStrikeout':'Strikethrough'}
TD=[[{'n':N[i],'l':asset(f'svg/light/toolbars/tool-{i}.svg'),'d':asset(f'svg/dark/toolbars/tool-{i}.svg')} for i in tab] for tab in PICK]
t=t.replace('__TOOLDATA__',json.dumps(TD))
t=re.sub(r'(src|data-d)="([^"$]+?)"',lambda m:f'{m.group(1)}="{asset(m.group(2))}"',t)
t=re.sub(r'url\((a/[^)]+)\)',lambda m:f'url({asset(m.group(1))})',t)
css=open('kit/thiran-ui.css').read()
css=re.sub(r"url\(['\"]?(fonts/[^)'\"]+)['\"]?\)",lambda m:f'url({os.path.basename(asset(os.path.join("kit",m.group(1))))})',css)
open(os.path.join(A,'thiran-ui.css'),'w').write(css)
t=t.replace('<link rel="stylesheet" href="kit/thiran-ui.css">','<link rel="stylesheet" href="assets/thiran-ui.css">')
t=t.replace('<title>Thiran home v7</title>','<title>Thiran: PDF markup and takeoff for construction</title>\n<meta name="description" content="Mark up, measure and review construction drawings in one place. Try every feature free for 7 days, no card needed.">\n<link rel="icon" href="'+asset('png/light/brand/brand-mark-m1--48@1x.png')+'">')
open(os.path.join(OUT,'index.html'),'w').write(t)
