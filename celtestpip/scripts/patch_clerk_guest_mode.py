import re

def patch_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if old in c:
        c = c.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Patched: {path}")
        return True
    else:
        print(f"Target not found in: {path}")
        return False

# 1. Patch ClerkLoading and ClerkLoaded in 3vbsvsuk3rveg.js
target_loading = '"s",0,({children:e})=>((0,t.t)("ClerkLoading"),"loading"!==(0,t.n)().status)?null:e'
repl_loading = '"s",0,({children:e})=>((0,t.t)("ClerkLoading"),null)'
patch_file('celtestpip/static/_next/static/immutable/chunks/3vbsvsuk3rveg.js', target_loading, repl_loading)

target_loaded = '"o",0,({children:e})=>((0,t.t)("ClerkLoaded"),(0,t.n)().loaded)?e:null'
repl_loaded = '"o",0,({children:e})=>((0,t.t)("ClerkLoaded"),e)'
patch_file('celtestpip/static/_next/static/immutable/chunks/3vbsvsuk3rveg.js', target_loaded, repl_loaded)

# 2. Patch useUser in 1lrrm53abg01o.js
target_useuser = 'void 0===e)?{isLoaded:!1,isSignedIn:void 0,user:void 0}:null===e?{isLoaded:!0,isSignedIn:!1,user:null}:{isLoaded:!0,isSignedIn:!0,user:e}'
repl_useuser = 'void 0===e)?{isLoaded:!0,isSignedIn:!1,user:null}:null===e?{isLoaded:!0,isSignedIn:!1,user:null}:{isLoaded:!0,isSignedIn:!0,user:e}'
patch_file('celtestpip/static/_next/static/immutable/chunks/1lrrm53abg01o.js', target_useuser, repl_useuser)

# 3. Patch listening.html to eliminate remote ui.browser.js preload and stub __internal_ClerkUICtor
target_preload = '<link rel="preload" href="https://clerk.celtestpip.com/npm/@clerk/ui@1/dist/ui.browser.js" as="script" crossorigin="anonymous"/>'
repl_preload = '<script>window.__internal_ClerkUICtor=function(){};</script>'
patch_file('celtestpip/data/pages/listening.html', target_preload, repl_preload)
