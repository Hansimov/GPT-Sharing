# how to make a graphics ve...

> how to make a graphics vertical center in latex beamer frame? Codes in tripple backticks is the graphics:
> ```
>   \includegraphics[width=0.32\textwidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
> ```

You can vertically center a graphic in a LaTeX beamer frame by using the `minipage` environment. Here’s an example:

    \begin{frame}[c]
      \begin{minipage}[c][\textheight][c]{\linewidth}
        \includegraphics[width=0.32\textwidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
    \end{frame}
    

This will center the graphic both horizontally and vertically on the frame[1](https://tex.stackexchange.com/questions/247826/beamer-full-vertical-centering).

1. [beamer full vertical centering - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/247826/beamer-full-vertical-centering)
2. [vertical alignment - Positioning content at the top of a beamer slide ...](https://tex.stackexchange.com/questions/9889/positioning-content-at-the-top-of-a-beamer-slide-by-default)
3. [A Beamer Tutorial in Beamer - Cornell University](https://people.orie.cornell.edu/jmd388/design/guides/Beamer%20Tutorial.pdf)
4. [Beamer - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/Beamer%23Creating_a_table_of_contents)

> how about there are sever graphics? I would like to put them side by side , and all vertical center

You can place several graphics side by side and vertically center them by using the `minipage` environment for each graphic. Here’s an example:

    \begin{frame}[c]
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
    \end{frame}
    

This will place three graphics side by side and vertically center them on the frame.

> how to determine the linewidth value adaptively, according to the hight and width of the graphics

The `linewidth` value is determined by the width of the line in which the `minipage` environment is placed. In the example I provided earlier, each `minipage` environment has a width of `0.32\linewidth`, which means it will take up 32% of the available line width.

If you want to adaptively determine the width of each `minipage` environment based on the height and width of the graphics, you can use the `calc` package to perform calculations with lengths. Here’s an example:

    \usepackage{calc}
    ...
    \newlength{\graphicheight}
    \settoheight{\graphicheight}{\includegraphics{./tikz-prompt-workflow-common.pdf}}
    \newlength{\graphicwidth}
    \settowidth{\graphicwidth}{\includegraphics{./tikz-prompt-workflow-common.pdf}}
    ...
    \begin{frame}[c]
      \begin{minipage}[c][\textheight][c]{\graphicwidth*\ratio{\textwidth}{3*\graphicwidth+\textwidth}}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{\graphicwidth*\ratio{\textwidth}{3*\graphicwidth+\textwidth}}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{\graphicwidth*\ratio{\textwidth}{3*\graphicwidth+\textwidth}}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
    \end{frame}
    

This will calculate the width of each `minipage` environment based on the width of the graphic and the available text width.

> how to use `foreach` grammer to refactor this

You can use the `pgffor` package to use a `foreach` loop in LaTeX. Here’s an example that refactors the previous example using a `foreach` loop:

    \usepackage{pgffor}
    ...
    \begin{frame}[c]
      \foreach \graphic in {./tikz-prompt-workflow-common.pdf, ./tikz-prompt-workflow-common.pdf, ./tikz-prompt-workflow-common.pdf} {
        \begin{minipage}[c][\textheight][c]{0.32\linewidth}
          \includegraphics[width=\linewidth,keepaspectratio]{\graphic}
        \end{minipage}
        \hfill
      }
    \end{frame}
    

This will produce the same result as the previous example but with less code.

> what does params in minpage mean?

The `minipage` environment takes several parameters that determine its behavior. Here’s what each parameter in the examples I provided earlier means:

-   The first parameter `[c]` specifies the vertical alignment of the content within the `minipage`. In this case, `c` stands for “center”, which means the content will be vertically centered within the `minipage`.
-   The second parameter `[\textheight]` specifies the height of the `minipage`. In this case, we set it to `\textheight`, which is the height of the text area on the page.
-   The third parameter `[c]` specifies the inner position of the content within the `minipage`. In this case, `c` stands for “center”, which means the content will be placed in the center of the `minipage`.
-   The fourth parameter `{0.32\linewidth}` specifies the width of the `minipage`. In this case, we set it to `0.32\linewidth`, which means it will take up 32% of the available line width.

You can adjust these parameters to change the behavior of the `minipage` environment and achieve different layouts.

> How to remove the blank or margin at top of minipage

If you want to remove the blank space or margin at the top of a `minipage` environment, you can use the `\vspace` command with a negative value. Here’s an example:

    \begin{frame}[c]
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \vspace{-\topskip}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \vspace{-\topskip}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
      \hfill
      \begin{minipage}[c][\textheight][c]{0.32\linewidth}
        \vspace{-\topskip}
        \includegraphics[width=\linewidth,keepaspectratio]{./tikz-prompt-workflow-common.pdf}
      \end{minipage}
    \end{frame}
    

This will remove the blank space at the top of each `minipage` environment.