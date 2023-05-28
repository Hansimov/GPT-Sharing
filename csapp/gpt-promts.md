You are a professional programmer and tech presentation maker.
I would like to make a presentation about how to use chatgpt to help programming in coding lifecyle. Please give an outline to me.


Please reformat your answer to a two-level structure. An example is here, delimited by three backquotes : ```1. Planning and Analysis 1.1 requirements analysis 1.2 feasible solutions 2. Design 2.1 architecture and components of the system 2.2 defining the APIs ... ```


I would like to teach programmers how to use chatgpt and bing ai to help programming. The contents between three backticks is a draft of my outline in latex beamer codes. Please Do Steps: (1) give some suggestions about the outline, (2) focusing on how to use chatgpt ```\section{Lifecycle of Coding} \section{Prompt Engineering} \section{Extensions and Plugins} \section{Ecosystem} \section{Websites} \section{Limitations}```

Please Do following instructions step by step:

(1) Draw a annular cyclical flowchart with latex TikZ for the relationships indicated in double quotes. "Requirement Analysis -> Design -> Implementation -> Testing and Integration -> Maintenance"
(2) Wrap texts in to arrow shaped nodes
(3) Fit node margin with text width

Use mindmap library in tikz to refactor you tikz codes

Please re-improve the paths connections between circles: Here is the grammer: `circle connection bar switch color=from (⟨first color⟩) to (⟨second color⟩)`, And here is an example: ` \path (n1) to[circle connection bar switch color=from (red) to (blue)] (n2);`

Use Tree Edges to re-improve your codes, here is an example: ``` child[concept color=blue] { node[concept] {applied} [clockwise from=-30] child { node[concept] {databases} } child { node[concept] {WWW} } } ```

1st, You should remove all codes similar to following: ```\path (root) to[circle connection bar switch color=from (red) to (blue)] (ra);```, because it no longer needed. 2nd, you should make subchildren has same color to its parent

1st, you should remove all color configs similar to ```concept color=purple!50``` in subchildren, as they are already inherited. 2nd, you should use sibling angle in style definitions to auto adjust the angle of subchildren, here is an example: ```level 1 concept/.append style={sibling angle=45},```