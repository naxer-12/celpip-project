import os

CHUNKS = [
    'celtestpip/static/_next/static/immutable/chunks/03_juy156wnoz.js',
    'celtestpip/static/_next/static/immutable/chunks/0qswil83_tm2g.js',
    'celtestpip/static/_next/static/immutable/chunks/1l5n8qyk3zp57.js',
    'celtestpip/static/_next/static/immutable/chunks/2kq2hj2tjrzmi.js'
]

def patch_file(filepath):
    with open(filepath, 'r') as f:
        c = f.read()
    
    # Replace loader button
    # Pattern 1: !N&&(0,t.jsx)(i.Button,{variant:"white",className:"flex lg:w-[128px] w-[80px]",children:(0,t.jsx)(m.Loader2,{className:"w-4 h-4 animate-spin text-zinc-600"})})
    import re
    # Match any !<var>&&(0,<t>.jsx)(<btn>.Button,{variant:"white",className:"flex lg:w-[128px] w-[80px]",children:(0,<t>.jsx)(<m>.Loader2,{className:"w-4 h-4 animate-spin text-zinc-600"})})
    loader_pattern = r'![a-zA-Z0-9_]+&&(\(0,[a-zA-Z0-9_]+\.jsx\)\([a-zA-Z0-9_]+\.Button,\{variant:\"white\",className:\"flex lg:w-\[128px\] w-\[80px\]\",children:\(0,[a-zA-Z0-9_]+\.jsx\)\([a-zA-Z0-9_]+\.Loader2,\{className:\"w-4 h-4 animate-spin text-zinc-600\"\}\)\}\))'
    
    # Also find the sign-in button check: !<signedIn>&&<isLoaded>&&(0,<t>.jsx)("div",{className:"flex gap-2"
    signin_pattern = r'(![a-zA-Z0-9_]+)&&[a-zA-Z0-9_]+&&(\(0,[a-zA-Z0-9_]+\.jsx\)\(\"div\",\{className:\"flex gap-2\")'
    
    c_new = re.sub(signin_pattern, r'\1&&\2', c)
    c_new = re.sub(loader_pattern, r'false&&\1', c_new)
    
    if c_new != c:
        with open(filepath, 'w') as f:
            f.write(c_new)
        print(f"Successfully patched {filepath}")
        return True
    else:
        print(f"No changes in {filepath}")
        return False

if __name__ == '__main__':
    for path in CHUNKS:
        patch_file(path)
