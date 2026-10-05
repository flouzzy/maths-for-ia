import re

with open('jalon-81/jalon-81.tex', 'r') as f:
    content = f.read()

# Fix the section issue: \section{Title }$L^2$ -> \section{Title $L^2$}
content = re.sub(r'\\(section|subsection|subsubsection)\*?\{(.*?)\s*\}(\$[^$]+\$)', r'\\\1{\2 \3}', content)
content = re.sub(r'\\(section|subsection|subsubsection)\*?\{(.*?)\}(\$[^$]+\$)', r'\\\1{\2 \3}', content)
content = re.sub(r'\\(section|subsection|subsubsection)\*?\{(.*?)\s*\}(L\^2)', r'\\\1{\2 \3}', content)


with open('jalon-81/jalon-81.tex', 'w') as f:
    f.write(content)
