import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHUNKS_DIR = os.path.join(BASE_DIR, "static", "_next", "static", "immutable", "chunks")

def patch_file(filename, replacements):
    path = os.path.join(CHUNKS_DIR, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename}: not found")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for target, replacement in replacements:
        if target in content:
            content = content.replace(target, replacement)
            modified = True
            print(f"Patched {filename}: replaced '{target[:30]}...'")
        else:
            print(f"Target not found in {filename}: '{target[:40]}...'")
            
    if modified:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully saved {filename}")

def main():
    # 1. 1hqel2llswsmf.js (speaking recorder ef)
    patch_file("1hqel2llswsmf.js", [
        (
            "function ef({durationLimit:e,prepTime:s,practice:a,userCredits:i,isPremium:l,isBlurred:o,isLoggedIn:u,userId:x,onSubmissionComplete:m}){",
            "function ef({durationLimit:e,prepTime:s,practice:a,userCredits:i,isPremium:l,isBlurred:o,isLoggedIn:u,userId:x,onSubmissionComplete:m}){o=false;l=true;i=999;u=true;if(!x)x=\"tester\";"
        )
    ])

    # 2. 3yh3c6tlpfetc.js (practice sidebar / list)
    patch_file("3yh3c6tlpfetc.js", [
        ("function z({parts:e,isPremium:i}){", "function z({parts:e,isPremium:i}){i=true;"),
        ("function R({parts:e,isPremium:i}){", "function R({parts:e,isPremium:i}){i=true;"),
        ("default\",0,function({parts:e,isPremium:i,isLoggedIn:s}){", "default\",0,function({parts:e,isPremium:i,isLoggedIn:s}){i=true;s=true;")
    ])

    # 3. 40cixahfxu4ls.js (mock exam launch)
    patch_file("40cixahfxu4ls.js", [
        (
            "default\",0,function({mockExam:e,isLoggedIn:u,isPremium:x,isNew:f}){",
            "default\",0,function({mockExam:e,isLoggedIn:u,isPremium:x,isNew:f}){u=true;x=true;"
        )
    ])

    # 4. 2fvw__nnw3kbd.js (PremiumProvider & usePremium)
    patch_file("2fvw__nnw3kbd.js", [
        ("createContext)({isPremium:!1})", "createContext)({isPremium:!0})"),
        ("PremiumProvider\",0,function({isPremium:e,children:s}){", "PremiumProvider\",0,function({isPremium:e,children:s}){e=true;"),
        ("usePremium\",0,function(){", "usePremium\",0,function(){return{isPremium:!0};")
    ])

    # 5. 0uicoa521uwuu.js (courses/lessons unlock)
    patch_file("0uicoa521uwuu.js", [
        (
            "default\",0,function({section:e,userId:c,courseSlug:p,isPremium:x,lessonNumber:u,totalLessons:m}){",
            "default\",0,function({section:e,userId:c,courseSlug:p,isPremium:x,lessonNumber:u,totalLessons:m}){x=true;c=\"tester\";"
        ),
        (
            "function b({courseSlug:e,courseTitle:r,navigation:o,isPremium:l,lessonNumber:a,totalLessons:d}){",
            "function b({courseSlug:e,courseTitle:r,navigation:o,isPremium:l,lessonNumber:a,totalLessons:d}){l=true;"
        )
    ])

    # 6. 07b_xsdyq1cal.js (practices catalog filter)
    patch_file("07b_xsdyq1cal.js", [
        (
            "function h({practice:e,partType:o,isLoggedIn:n,isPremium:m,index:f,isWritingTask1:b,highlightType:x}){",
            "function h({practice:e,partType:o,isLoggedIn:n,isPremium:m,index:f,isWritingTask1:b,highlightType:x}){m=true;n=true;"
        ),
        (
            "default\",0,function({practices:e,partType:l,isLoggedIn:a,isPremium:i,taskSlug:s}){",
            "default\",0,function({practices:e,partType:l,isLoggedIn:a,isPremium:i,taskSlug:s}){i=true;a=true;"
        )
    ])

    # 7. 3vuqpyt93s71e.js (silence excessive viewport prefetching to eliminate network storms)
    patch_file("3vuqpyt93s71e.js", [
        (
            "function b(t,r){if(\"u\">typeof window){",
            "function b(t,r){return;if(\"u\">typeof window){"
        )
    ])

    # 8. 151vlzb53x6r3.js (vocabulary bundle unlock, no blurred words, no locked words, no subscription modal)
    patch_file("151vlzb53x6r3.js", [
        (
            "({words:e,bundleId:r,bundleSlug:l,isPremium:o,isFree:c,isLoggedIn:d,totalWords:m,barColor:h})=>{",
            "({words:e,bundleId:r,bundleSlug:l,isPremium:o,isFree:c,isLoggedIn:d,totalWords:m,barColor:h})=>{o=true;c=true;d=true;e=(e||[]).map(w=>({...w,locked:false}));m=e.length;"
        ),
        (
            "{openSubscriptionModal:T}=(0,p.useSubscriptionModal)()",
            "{openSubscriptionModal:_rawT}=(0,p.useSubscriptionModal)(),T=()=>{}"
        ),
        (
            "O=async e=>{if(e.locked)return void T(\"word_bundle\");if(!d)return void M(\"Log in to Continue\",\"Please login to learn words and track your progress.\");",
            "O=async e=>{e.locked=false;d=true;"
        )
    ])

    # 9. 3fvl1-fzhlq7v.js (reading/writing practice prompt unblur and blocker removal)
    patch_file("3fvl1-fzhlq7v.js", [
        (
            "function({practice:e,hasAccess:x,lockedSource:f,lockedNote:g=!0,leftExtra:b,belowOnMobile:w,children:j}){x=true;",
            "function({practice:e,hasAccess:x,lockedSource:f,lockedNote:g=!0,leftExtra:b,belowOnMobile:w,children:j}){x=true;g=false;"
        ),
        (
            "children:[e.slice(0,110),(0,t.jsx)(\"span\",{className:\"text-zinc-500 blur-sm\",children:b.loremIpsum})]",
            "children:[e]"
        ),
        (
            "children:[(e.text??\"\").slice(0,110),(0,t.jsx)(\"span\",{className:\"text-zinc-500 blur-sm\",children:o.loremIpsum})]",
            "children:[e.text??\"\"]"
        )
    ])

    # 10. 2uolzeil_hqy7.js (PDF / study documents viewer unlock)
    patch_file("2uolzeil_hqy7.js", [
        ("\"login\"===e.locked?\"Sign in to read\":\"Upgrade to Pro\"", "\"Read Document\""),
        ("a?\"This document is for Pro members\":\"Sign in to read this document\"", "\"CELTESTPIP Study Document\""),
        ("(\"PUBLIC\"===e.access?", "(true?")
    ])

if __name__ == "__main__":
    main()
