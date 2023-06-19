# I would like to add my pe...

> I would like to add my personal completion suggestions in vscode, just like the its built-in completion for different programming languages, how could i do this?

You can add your personal completion suggestions in Visual Studio Code by providing a typings file with the definitions from your modules and making it available to Visual Studio Code. [It will then show the info in its normal completion suggestions](https://stackoverflow.com/questions/63196508/custom-intellisense-auto-completion-in-vscode-how-to-dynamically-point-intellis)[1](https://stackoverflow.com/questions/63196508/custom-intellisense-auto-completion-in-vscode-how-to-dynamically-point-intellis). [You can also use the `vscode.languages.registerInlineCompletionItemProvider` method to provide inline completion items](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)[2](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode). Is there a specific language or file type you want to add completion suggestions for?

1. [javascript - Custom intellisense auto completion in vscode: how to ...](https://stackoverflow.com/questions/63196508/custom-intellisense-auto-completion-in-vscode-how-to-dynamically-point-intellis)
2. [How to trigger "inline suggestion" in VSCode? - Stack Overflow](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)
3. [](https://bing.com/search?q=add+personal+completion+suggestions+vscode)
4. [IntelliSense in Visual Studio Code](https://code.visualstudio.com/docs/editor/intellisense)
5. [VSCode how to automatically insert Intellisense suggestions without ...](https://stackoverflow.com/questions/61078606/vscode-how-to-automatically-insert-intellisense-suggestions-without-having-to-pr)
6. [Enabling the Schema on VS Code - DEV Community](https://dev.to/brpaz/how-to-create-your-own-auto-completion-for-json-and-yaml-files-on-vs-code-with-the-help-of-json-schema-k1i)

> Let me clarify my requirements. I will type some characters, and then the vscode will show a list of suggestions, and i can select one of them to complete my typing.
> Then how could i add my customized word or sentence suggestions list to vscode?

You can add custom word or sentence suggestions to Visual Studio Code by writing a custom snippet. You can do this by using the `Snippets: Configure User Snippets` command in the command palette. For example, if you want to add a suggestion that changes “key” into “key hole”, you can write a custom snippet like this[1](https://stackoverflow.com/questions/76213722/how-can-i-add-custom-suggestions-in-vs-code):

    {
        "key": {
            "prefix": "key",
            "body": "key hole"
        }
    }
    

Copy

Is this what you were looking for?

1. [How can I add custom suggestions in VS Code? - Stack Overflow](https://stackoverflow.com/questions/76213722/how-can-i-add-custom-suggestions-in-vs-code)
2. [IntelliSense in Visual Studio Code](https://code.visualstudio.com/docs/editor/intellisense)
3. [How to trigger "inline suggestion" in VSCode? - Stack Overflow](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)
4. [Markdown editing with Visual Studio Code](https://code.visualstudio.com/Docs/languages/markdown)
5. [how to highlight user specified words in vscode - Stack Overflow](https://stackoverflow.com/questions/58174681/how-to-highlight-user-specified-words-in-vscode)

> Great! I create a `gpt.code-snippets` in my vscode snippets path.
> Below is its initial content, how could i add some of my customized snippets?
> For example, I would like to enable the snippet only for `.txt` formats, then when i type "i", it would show "I would like to ...".

You can add your custom snippet to the `gpt.code-snippets` file by adding a new entry to the JSON object. For example, to enable the snippet only for `.txt` formats and have it show “I would like to …” when you type “i”, you can add the following entry:

    {
        "I would like to": {
            "scope": "plaintext",
            "prefix": "i",
            "body": [
                "I would like to $1"
            ],
            "description": "Insert 'I would like to'"
        }
    }
    

Copy

This will create a new snippet with the prefix `i` that is only available in plaintext files (`.txt` files). When you type `i`, it will show the suggestion “I would like to …”. Is this what you were looking for?

> Great! Then I would like to make the snippets also show just besides the inline cursor when typing, how to do this?

By default, snippets appear in IntelliSense (Ctrl+Space) mixed with other suggestions. [You can also trigger them by typing the snippet prefix (trigger text) and pressing Tab if you have enabled tab completion with `"editor.tabCompletion": "on"`](https://code.visualstudio.com/docs/editor/userdefinedsnippets)[1](https://code.visualstudio.com/docs/editor/userdefinedsnippets). This will show the suggestions in a widget, but not inline with the cursor.

Unfortunately, I couldn’t find any information on how to show custom snippets inline with the cursor while typing. Is there anything else I can help you with?

1. [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)
2. [How can I set the cursor selection for snippet in vscode?](https://stackoverflow.com/questions/69342514/how-can-i-set-the-cursor-selection-for-snippet-in-vscode)
3. [Code snippets - Visual Studio (Windows) | Microsoft Learn](https://learn.microsoft.com/en-us/visualstudio/ide/code-snippets?view=vs-2022)
4. [Bug in cursor location within user snippets #11742 - GitHub](https://github.com/Microsoft/vscode/issues/11742)
5. [Walkthrough: Create a code snippet in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/walkthrough-creating-a-code-snippet?view=vs-2022)

> Great! Then how to make the suggestions show immediately when typing, without pressing `Ctrl+Space`?

You can make suggestions show immediately when typing by enabling quick suggestions in your settings. To do this, go to `Settings` by pressing `Ctrl + ,` and type in `quick suggestions`. [Then, edit the item labeled `other` and select the `inline` value](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)[1](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode). This will make code suggestions appear inline as you type.

Is this what you were looking for?

1. [How to trigger "inline suggestion" in VSCode? - Stack Overflow](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)
2. [Visual Studio Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
3. [](https://bing.com/search?q=show+suggestions+immediately+when+typing+vscode)
4. [IntelliSense in Visual Studio Code](https://code.visualstudio.com/docs/editor/intellisense)
5. [VS Code: How to Disable/Enable Suggestions on Hover](https://www.kindacode.com/article/vs-code-how-to-disable-enable-suggestions-on-hover/)
6. [IntelliCode suggestions - Visual Studio IntelliCode | Microsoft Learn](https://learn.microsoft.com/en-us/visualstudio/intellicode/intellicode-suggestions)

> Then how to auto enable the action of "Trigger Suggest" without hitting `Ctrl+Space`?

You can enable quick suggestions to show suggestions immediately when typing. To do this, go to `Settings` by pressing `Ctrl + ,` and type in `quick suggestions`. Then, edit the item labeled `other` and set it to `true`[1](https://code.visualstudio.com/Docs/languages/html). This will make suggestions appear automatically as you type.

Is this what you were looking for?

1. [HTML Programming with Visual Studio Code](https://code.visualstudio.com/Docs/languages/html)
2. [](https://bing.com/search?q=auto+enable+trigger+suggest+vscode)
3. [IntelliSense in Visual Studio Code](https://code.visualstudio.com/docs/editor/intellisense)
4. [How to trigger "inline suggestion" in VSCode? - Stack Overflow](https://stackoverflow.com/questions/68263285/how-to-trigger-inline-suggestion-in-vscode)
5. [Can GitHub Copilot stop auto-suggesting, instead be triggered by a ...](https://stackoverflow.com/questions/71224911/can-github-copilot-stop-auto-suggesting-instead-be-triggered-by-a-keystroke)
6. [How to control Trigger Inline Suggestions in VSCode? – Tabnine](https://support.tabnine.com/hc/en-us/articles/13965663739921-How-to-control-Trigger-Inline-Suggestions-in-VSCode-)

> Great! I have created some snippets, then how to make the completion case insensitive?

I’m sorry, but I couldn’t find any information on how to make completion case insensitive in Visual Studio Code. Is there anything else I can help you with?

1. [Autocomplete should be case insensitive for suggesting strings](https://github.com/Microsoft/vscode/issues/8395)
2. [VS Code extension, how to make case insensitive?](https://stackoverflow.com/questions/50314380/vs-code-extension-how-to-make-case-insensitive)
3. [Case-insensitive code completion – IDEs Support (IntelliJ Platform ...](https://intellij-support.jetbrains.com/hc/en-us/community/posts/205806989-Case-insensitive-code-completion)
4. [Make snippet selection case sensitive · Issue #8070 · microsoft/vscode](https://github.com/Microsoft/vscode/issues/8070)
5. [Case-sensitive multiselect in VS Code · J Ben Deaton](https://jbendeaton.com/blog/2020/case-sensitive-multiselect-in-vscode)