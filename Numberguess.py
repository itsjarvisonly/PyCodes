text = "X-DSPAM-Confidence:   0.8475"
atpos = text.find(":")
end = len(text)
show = text[atpos+4:end+1]
print(show)