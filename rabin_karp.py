t = """Психологически почти все они были рабами — рабами веры, 
рабами себе подобных, рабами страстишек, рабами корыстолюбия. 
И если волею судеб кто-нибудь рождался или становился господином, 
он не знал, что делать со своей свободой. Он снова торопился 
стать рабом — рабом богатства, рабом противоестественных излишеств, 
рабом распутных друзей, рабом своих рабов."""
p = "раб"

def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s) for s in pattern)
    for n in range(len(text) - len(pattern) + 1):
        textwindowsum = sum(ord(text[i+n]) for i in range(len(pattern)))
        if textwindowsum == patternsum:
            if text.startswith(pattern, n):
                result.append(n)
    return result

print(find_all_rabin_karp(t, p))