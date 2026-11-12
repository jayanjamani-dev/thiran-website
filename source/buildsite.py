import re,os,json,shutil,hashlib,sys
from PIL import Image
OUT=sys.argv[1]; t=open('v8.tpl.html').read()
t=t.replace('__BOOKDEMO__',open('book-demo.part.html').read())
A=os.path.join(OUT,'assets'); os.makedirs(A,exist_ok=True)
cache={}; DIM={}
def asset(p):
    if p in cache: return cache[p]
    if p.startswith(('data:','http','${','#','/')): return p
    rp=os.path.realpath(p); base=os.path.basename(p).replace('@1x','')
    stem,ext=os.path.splitext(base); h=hashlib.md5(open(rp,'rb').read()).hexdigest()[:8]
    if ext.lower() in ('.jpg','.jpeg','.png') and 'brand-mark' not in stem:
        # every photo and screen goes out as WebP (alpha kept for PNGs)
        name=f'{stem}-{h}.webp'; im=Image.open(rp)
        im=im.convert('RGBA' if im.mode in ('RGBA','LA','P') else 'RGB')
        if im.width>2400 and not stem.startswith(('hero-lap3','hero-lap4','hero-full')): im=im.resize((2400,round(im.height*2400/im.width)),Image.LANCZOS)
        q=88 if stem.startswith('hero-full') else 80 if stem.startswith('hero-lap') else 84
        im.save(os.path.join(A,name),quality=q,method=6)
    else:
        name=f'{stem}-{h}{ext}'; shutil.copy(rp,os.path.join(A,name))
    if ext.lower() in ('.jpg','.jpeg','.png','.gif','.webp'): DIM['assets/'+name]=Image.open(rp).size
    cache[p]='assets/'+name; return cache[p]
PICK=[['text','callout','cloud','pen','highlighter','arrow','rectangle','dimension'],['length','polylength','area','count','volume','dynamicFill','visualSearch','lineTrace'],['stamp','signature','image','snapshot','photo','table','legend','tag'],['cloud','callout','note','approval','stamp','textHighlight','textUnderline','textStrikeout']]
N={'text':'Text box','callout':'Callout','cloud':'Cloud','pen':'Pen','highlighter':'Highlighter','arrow':'Arrow','rectangle':'Rectangle','dimension':'Dimension','length':'Length','polylength':'Run length','area':'Area','count':'Count','volume':'Volume','dynamicFill':'Fill Area','visualSearch':'Find Similar','lineTrace':'Service takeoff','stamp':'Stamp','signature':'Signature','image':'Image','snapshot':'Snapshot','photo':'Photo pin','table':'Schedule','legend':'Legend','tag':'Label','note':'Sticky note','approval':'Approval stamp','textHighlight':'Highlight text','textUnderline':'Underline','textStrikeout':'Strikethrough'}
TD=[[{'n':N[i],'l':asset(f'svg/light/toolbars/tool-{i}.svg'),'d':asset(f'svg/dark/toolbars/tool-{i}.svg')} for i in tab] for tab in PICK]
t=t.replace('__TOOLDATA__',json.dumps(TD))
t=re.sub(r'(src|data-d)="([^"$]+?)"',lambda m:f'{m.group(1)}="{asset(m.group(2))}"',t)
t=re.sub(r'url\((a/[^)]+)\)',lambda m:f'url({asset(m.group(1))})',t)
HERO_END=t.index('<!-- PEOPLE -->')
def imgtag(m):
    tag=m.group(0); src=re.search(r'src="([^"]+)"',tag)
    if not src: return tag
    if ' width=' not in tag and src.group(1) in DIM:
        w,h=DIM[src.group(1)]; tag=tag.replace('<img ',f'<img width="{w}" height="{h}" ',1)
    if m.start()>HERO_END and 'loading=' not in tag: tag=tag.replace('<img ','<img loading="lazy" decoding="async" ',1)
    return tag
t=re.sub(r'<img [^>]*>',imgtag,t)
css=open('kit/thiran-ui.css').read()
css=re.sub(r"url\(['\"]?(fonts/[^)'\"]+)['\"]?\)",lambda m:f'url({os.path.basename(asset(os.path.join("kit",m.group(1))))})',css)
open(os.path.join(A,'thiran-ui.css'),'w').write(css)
t=t.replace('<link rel="stylesheet" href="kit/thiran-ui.css">','<link rel="stylesheet" href="assets/thiran-ui.css">')
ICON=asset('png/light/brand/brand-mark-m1--48@1x.png')
t=t.replace('<title>Thiran home v7</title>',open('head.html').read().replace('__ICON__',ICON))
open(os.path.join(OUT,'.icon'),'w').write('/'+ICON)
open(os.path.join(OUT,'index.html'),'w').write(t)
