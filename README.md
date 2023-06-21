# GPT-Sharing
Presentations for GPT training and sharing with experienced software Engineers

* Prompts Cheat Sheet (Group by Principles):
  * https://hansimov.github.io/GPT-Sharing/prompts-cheat-sheet.html

* Slides: Prompt Techniques
  * https://hansimov.github.io/GPT-Sharing/slides/prompt-techniques.html


## Commands

Install packages:

```bash
# [./slides]:
npm install
npm install -g decktape
```

Run local server to real-time preview slides:

```bash
# [./slides]:
npm start -- --port 8888
```

Export to PDF:

```bash
decktape automatic http://localhost:8888/prompt-techniques.html prompt-techniques.pdf
```
