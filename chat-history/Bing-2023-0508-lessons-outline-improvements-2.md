# 



> In beamer, how to create sub-title page ?

In Beamer, you can set the subtitle using the `subtitle{...}` command (not inside the title page!). If you’d like to insert the subtitle in a custom title page, you can use `insertsubtitle` (this macro does not have any arguments!) [1](https://stackoverflow.com/questions/75200512/how-to-customize-the-title-page-of-beamer-presentation). Is there anything else you would like to know?

1. [How to customize the title page of beamer presentation?](https://stackoverflow.com/questions/75200512/how-to-customize-the-title-page-of-beamer-presentation)
2. [titles - How to customize \titlepage in beamer? - TeX - LaTeX Stack ...](https://tex.stackexchange.com/questions/22346/how-to-customize-titlepage-in-beamer)
3. [Automatically generate section title slides in beamer?](https://tex.stackexchange.com/questions/117658/automatically-generate-section-title-slides-in-beamer)
4. [Beamer title page to show subtitle on click - Stack Exchange](https://tex.stackexchange.com/questions/307198/beamer-title-page-to-show-subtitle-on-click)
5. [Beamer - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/Beamer%23Creating_a_table_of_contents)

> For example, I have lessons below in tripple backticks. How to add a title page with same main title but different subtitles for each lesson?
> ```
> % Lesson 1: Mastering Prompt Engineering: Principles, Techniques, and Extensions
> % Lesson 2: GPT in Action: Case Studies of Coding Tasks
> % Lesson 3: Enhancing Your Coding Workflow with GPT Integration
> % Lesson 4: Exploring Cutting-Edge GPT Projects and Showcases
> % Lesson 5: Unleashing the Power of GPT through Customization
> ```

You can create a title page for each lesson by using the `frame` environment and the `titlepage` command. For example:

    \documentclass{beamer}
    \title{Main Title}
    \author{Author Name}
    
    \begin{document}
    
    % Lesson 1
    \subtitle{Mastering Prompt Engineering: Principles, Techniques, and Extensions}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 2
    \subtitle{GPT in Action: Case Studies of Coding Tasks}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 3
    \subtitle{Enhancing Your Coding Workflow with GPT Integration}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 4
    \subtitle{Exploring Cutting-Edge GPT Projects and Showcases}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 5
    \subtitle{Unleashing the Power of GPT through Customization}
    \begin{frame}
    \titlepage
    \end{frame}
    
    \end{document}
    

This will create a title page for each lesson with the same main title but different subtitles. Is there anything else you would like to know?

> How to add a toc for these subtitles. Only provide codes added, do not show whole script.

You can add a table of contents for the subtitles by using the `section` command and the `tableofcontents` command. Here is the code you can add to your script:

    % Add sections for each lesson
    \section{Mastering Prompt Engineering: Principles, Techniques, and Extensions}
    \section{GPT in Action: Case Studies of Coding Tasks}
    \section{Enhancing Your Coding Workflow with GPT Integration}
    \section{Exploring Cutting-Edge GPT Projects and Showcases}
    \section{Unleashing the Power of GPT through Customization}
    
    % Add table of contents
    \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents
    \end{frame}
    

This will create a table of contents slide that lists all the subtitles. Is there anything else you would like to know?

> How to make `\section` use subtitles text, but no need to type whole line for each?

You can define a new command that takes the subtitle text as an argument and uses it to set both the subtitle and the section. Here is an example:

    % Define new command
    \newcommand{\lesson}[1]{\section{#1}\subtitle{#1}}
    
    % Use new command for each lesson
    \lesson{Mastering Prompt Engineering: Principles, Techniques, and Extensions}
    \lesson{GPT in Action: Case Studies of Coding Tasks}
    \lesson{Enhancing Your Coding Workflow with GPT Integration}
    \lesson{Exploring Cutting-Edge GPT Projects and Showcases}
    \lesson{Unleashing the Power of GPT through Customization}
    

This will set both the section and the subtitle for each lesson using the same text. Is there anything else you would like to know?

> Great! Could you also add `Lesson X` for x-th lesson in your command?

Sure! You can modify the new command to include a counter that increments for each lesson and adds the lesson number to the section title. Here is an example:

    % Define new counter
    \newcounter{lessoncounter}
    
    % Define new command
    \newcommand{\lesson}[1]{\stepcounter{lessoncounter}\section{Lesson \arabic{lessoncounter}: #1}\subtitle{#1}}
    
    % Use new command for each lesson
    \lesson{Mastering Prompt Engineering: Principles, Techniques, and Extensions}
    \lesson{GPT in Action: Case Studies of Coding Tasks}
    \lesson{Enhancing Your Coding Workflow with GPT Integration}
    \lesson{Exploring Cutting-Edge GPT Projects and Showcases}
    \lesson{Unleashing the Power of GPT through Customization}
    

This will set both the section and the subtitle for each lesson using the same text and add the lesson number to the section title. Is there anything else you would like to know?

> now with the improvements above, provide the whole script which contains title page for each subtitle

Here is the complete script that includes the improvements above and creates a title page for each subtitle:

    \documentclass{beamer}
    \title{Main Title}
    \author{Author Name}
    
    % Define new counter
    \newcounter{lessoncounter}
    
    % Define new command
    \newcommand{\lesson}[1]{\stepcounter{lessoncounter}\section{Lesson \arabic{lessoncounter}: #1}\subtitle{#1}}
    
    \begin{document}
    
    % Add sections for each lesson
    \lesson{Mastering Prompt Engineering: Principles, Techniques, and Extensions}
    \lesson{GPT in Action: Case Studies of Coding Tasks}
    \lesson{Enhancing Your Coding Workflow with GPT Integration}
    \lesson{Exploring Cutting-Edge GPT Projects and Showcases}
    \lesson{Unleashing the Power of GPT through Customization}
    
    % Add table of contents
    \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents
    \end{frame}
    
    % Lesson 1
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 2
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 3
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 4
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 5

> continue

Here is the rest of the script:

    \begin{frame}
    \titlepage
    \end{frame}
    
    \end{document}
    

This will create a title page for each lesson with the same main title but different subtitles and a table of contents slide that lists all the subtitles. Is there anything else you would like to know?

> 1st, shorten title for each topic;
> 2nd, you miss place the `\lesson` and `\begin{frame}`, they should put together.

I apologize for the mistake. Here is the corrected script that includes shortened titles for each topic and places the `\lesson` and `\begin{frame}` commands together:

    \documentclass{beamer}
    \title{Main Title}
    \author{Author Name}
    
    % Define new counter
    \newcounter{lessoncounter}
    
    % Define new command
    \newcommand{\lesson}[1]{\stepcounter{lessoncounter}\section{Lesson \arabic{lessoncounter}}\subtitle{#1}}
    
    \begin{document}
    
    % Add table of contents
    \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents
    \end{frame}
    
    % Lesson 1
    \lesson{Mastering Prompt Engineering}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 2
    \lesson{GPT in Action}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 3
    \lesson{Enhancing Your Coding Workflow}
    \begin{frame}
    \titlepage
    \end{frame}
    
    % Lesson 4
    \lesson{Exploring Cutting-Edge GPT Projects}
    \begin