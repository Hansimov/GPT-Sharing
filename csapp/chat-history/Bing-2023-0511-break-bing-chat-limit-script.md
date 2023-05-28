# The content below in trip...

> The content below in triple backticks is HTML codes.
> I would like to write a JavaScript script in the console of DevTool, so that I can change the max value of letter counter from 2000 to 20000.
> And should not change the effect of the countered value of typed letters, which starts from 0.
> 
> ```
> <div class="bottom-bar">
>     <div class="letter-counter"><span>0</span>/2000</div>
> </div>
> ```
> 
> Please provide me your JS codes.

You can use the following JavaScript code to change the max value of the letter counter from 2000 to 20000:

    let counter = document.querySelector('.letter-counter');
    counter.textContent = counter.textContent.replace('2000', '20000');
    

Copy

This code selects the element with the class `letter-counter` and replaces the text content of `2000` with `20000`. The effect of the countered value of typed letters, which starts from 0, should not be changed.

Is there anything else you would like to know?

> Your code gives me "caught TypeError: Cannot read properties of null (reading 'textContent')"

The error message you received indicates that the `counter` variable is `null`, which means that the `document.querySelector('.letter-counter')` did not find any element with the class `letter-counter`.

This could happen if the HTML code you provided is not present on the page when the JavaScript code is executed. Make sure that the HTML code is present on the page and that the JavaScript code is executed after the page has finished loading.

You can try wrapping the JavaScript code in a `window.onload` event to ensure that it is executed after the page has finished loading:

    window.onload = function() {
        let counter = document.querySelector('.letter-counter');
        counter.textContent = counter.textContent.replace('2000', '20000');
    }
    

Copy

Let me know if this helps.

> Two problems you should solve:
> (1) The letter-counte is hidden until user click the text area
> (2) The countered characters would not change again after seting the textContent

Thank you for letting me know about these issues.

(1) If the `letter-counter` element is hidden until the user clicks the text area, you can try adding an event listener to the text area that runs the JavaScript code when the text area is clicked. Here’s an example:

    let textarea = document.querySelector('textarea');
    textarea.addEventListener('click', function() {
        let counter = document.querySelector('.letter-counter');
        counter.textContent = counter.textContent.replace('2000', '20000');
    });
    

Copy

Make sure to replace `'textarea'` with the appropriate selector for the text area on your page.

(2) If the countered characters do not change after setting the `textContent`, it could be because the code that updates the countered characters is using a different method to access the max value of the letter counter. Without more information about how the countered characters are updated, it’s difficult for me to provide a solution. Can you provide more details about how the countered characters are updated?

> So if the code that updates the countered characters is using a different method to access the max value of the letter counter, how could I find the method, or just rewrite it by myself?

If the code that updates the countered characters is using a different method to access the max value of the letter counter, you can try to find the code that updates the countered characters and see how it accesses the max value. You can then modify that code to use the new max value of 20000.

To find the code that updates the countered characters, you can try searching the JavaScript files on your page for keywords related to updating the countered characters, such as `letter-counter`, `textContent`, or `innerHTML`. You can also try using the debugger in your browser’s developer tools to pause the execution of the JavaScript code when the countered characters are updated and see which code is being executed.

If you are unable to find or modify the code that updates the countered characters, you can try writing your own code to update the countered characters. You can add an event listener to the text area that listens for changes to its value and updates the countered characters accordingly. Here’s an example:

    let textarea = document.querySelector('textarea');
    let counter = document.querySelector('.letter-counter');
    let maxCount = 20000;
    
    textarea.addEventListener('input', function() {
        let currentCount = textarea.value.length;
        counter.textContent = currentCount + '/' + maxCount;
    });
    

Copy

Make sure to replace `'textarea'` with the appropriate selector for the text area on your page.

I hope this helps. Let me know if you have any further questions.

> Your solution is great!
> Here is my script, could you help improve it in two aspects: (1) make this script run until the `cib_bar_main` is created in the document; (2) make the script more clean:
> ```
> let cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
> let textarea = cib_bar_main.querySelector("textarea");
> let maxCount  = 20000;
> textarea.addEventListener('input', function() {
>     textarea.maxLength = maxCount;
>     let currentCount = textarea.value.length;
>     let counter = cib_bar_main.querySelector('.letter-counter');
>     counter.textContent = currentCount + '/' + maxCount;
> });
> ```

Here’s an improved version of your script that addresses the two aspects you mentioned:

    let maxCount = 20000;
    
    function updateLetterCounter() {
        let cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
        let textarea = cib_bar_main.querySelector("textarea");
        textarea.maxLength = maxCount;
        let currentCount = textarea.value.length;
        let counter = cib_bar_main.querySelector('.letter-counter');
        counter.textContent = currentCount + '/' + maxCount;
    }
    
    function initLetterCounter() {
        let cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
        if (cib_bar_main) {
            let textarea = cib_bar_main.querySelector("textarea");
            textarea.addEventListener('input', updateLetterCounter);
            updateLetterCounter();
        } else {
            setTimeout(initLetterCounter, 100);
        }
    }
    
    initLetterCounter();
    

Copy

This script uses two functions: `updateLetterCounter` and `initLetterCounter`. The `updateLetterCounter` function updates the letter counter with the current value of the text area and the max value of `maxCount`. The `initLetterCounter` function checks if the `cib_bar_main` element is present in the document. If it is present, it adds an event listener to the text area to update the letter counter when its value changes and calls the `updateLetterCounter` function to update the letter counter initially. If the `cib_bar_main` element is not present, it calls itself again after a delay of 100 milliseconds using `setTimeout`.

This script will run until the `cib_bar_main` element is created in the document and will add an event listener to the text area to update the letter counter when its value changes. The code is also organized into functions to make it cleaner and easier to understand.

I hope this helps. Let me know if you have any further questions.

> Great, But I only want to assign the value of `cib_bar_main` one time after it is created, and then no longer re-assign, and only change the textContent.

Here’s an updated version of the script that only assigns the value of `cib_bar_main` once after it is created and then only changes the `textContent` of the letter counter:

    let maxCount = 20000;
    let cib_bar_main;
    let textarea;
    let counter;
    
    function updateLetterCounter() {
        textarea.maxLength = maxCount;
        let currentCount = textarea.value.length;
        counter.textContent = currentCount + '/' + maxCount;
    }
    
    function initLetterCounter() {
        cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
        if (cib_bar_main) {
            textarea = cib_bar_main.querySelector("textarea");
            counter = cib_bar_main.querySelector('.letter-counter');
            textarea.addEventListener('input', updateLetterCounter);
            updateLetterCounter();
        } else {
            setTimeout(initLetterCounter, 100);
        }
    }
    
    initLetterCounter();
    

Copy

In this version of the script, the `cib_bar_main`, `textarea`, and `counter` variables are declared outside of the functions so that their values can be shared between the functions. The `initLetterCounter` function assigns the value of `cib_bar_main` only once after it is created and then assigns the values of `textarea` and `counter`. It also adds an event listener to the text area to update the letter counter when its value changes and calls the `updateLetterCounter` function to update the letter counter initially. The `updateLetterCounter` function uses the values of `textarea` and `counter` to update the letter counter without reassigning their values.

I hope this helps. Let me know if you have any further questions.

> Great! Improve your codes: Only run the initLetterCounter when the page is ready.

Here’s an updated version of the script that only runs the `initLetterCounter` function when the page is ready:

    let maxCount = 20000;
    let cib_bar_main;
    let textarea;
    let counter;
    
    function updateLetterCounter() {
        textarea.maxLength = maxCount;
        let currentCount = textarea.value.length;
        counter.textContent = currentCount + '/' + maxCount;
    }
    
    function initLetterCounter() {
        cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
        if (cib_bar_main) {
            textarea = cib_bar_main.querySelector("textarea");
            counter = cib_bar_main.querySelector('.letter-counter');
            textarea.addEventListener('input', updateLetterCounter);
            updateLetterCounter();
        } else {
            setTimeout(initLetterCounter, 100);
        }
    }
    
    document.addEventListener('DOMContentLoaded', initLetterCounter);
    

Copy

In this version of the script, an event listener is added to the `document` object to listen for the `DOMContentLoaded` event. When this event is triggered, it means that the page is ready and the `initLetterCounter` function is called. The rest of the script is unchanged from the previous version.

I hope this helps. Let me know if you have any further questions.

> I would like to wrap this script in a Tampermonkey script , please do this for me

Sure! Here’s a Tampermonkey script that wraps the previous JavaScript code:

    // ==UserScript==
    // @name         Letter Counter
    // @namespace    http://tampermonkey.net/
    // @version      1
    // @description  Update the max value of the letter counter to 20000
    // @match        YOUR_URL_HERE
    // @grant        none
    // ==/UserScript==
    
    (function() {
        'use strict';
    
        let maxCount = 20000;
        let cib_bar_main;
        let textarea;
        let counter;
    
        function updateLetterCounter() {
            textarea.maxLength = maxCount;
            let currentCount = textarea.value.length;
            counter.textContent = currentCount + '/' + maxCount;
        }
    
        function initLetterCounter() {
            cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
            if (cib_bar_main) {
                textarea = cib_bar_main.querySelector("textarea");
                counter = cib_bar_main.querySelector('.letter-counter');
                textarea.addEventListener('input', updateLetterCounter);
                updateLetterCounter();
            } else {
                setTimeout(initLetterCounter, 100);
            }
        }
    
        document.addEventListener('DOMContentLoaded', initLetterCounter);
    })();
    

Copy

Make sure to replace `YOUR_URL_HERE` with the URL of the page where you want to run this script. You can also update the `@name`, `@namespace`, `@description`, and other metadata fields as needed.

To use this script, you need to have the Tampermonkey extension installed in your browser. Then, you can create a new script in Tampermonkey and paste the above code into the script editor. Make sure to save the script and enable it on the page where you want it to run.

I hope this helps. Let me know if you have any further questions.

> this script should only work in the url like: `https://www.bing.com/search?toWww=1&redig=D94B455F41404090B72A729ED4DF03A2&q=Bing+AI&showconv=1`

To make the Tampermonkey script only work on URLs like the one you provided, you can update the `@match` field in the script’s metadata block to match the URL pattern. Here’s an updated version of the script that only runs on URLs that start with `https://www.bing.com/search`:

    // ==UserScript==
    // @name         Letter Counter
    // @namespace    http://tampermonkey.net/
    // @version      1
    // @description  Update the max value of the letter counter to 20000
    // @match        https://www.bing.com/search*
    // @grant        none
    // ==/UserScript==
    
    (function() {
        'use strict';
    
        let maxCount = 20000;
        let cib_bar_main;
        let textarea;
        let counter;
    
        function updateLetterCounter() {
            textarea.maxLength = maxCount;
            let currentCount = textarea.value.length;
            counter.textContent = currentCount + '/' + maxCount;
        }
    
        function initLetterCounter() {
            cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
            if (cib_bar_main) {
                textarea = cib_bar_main.querySelector("textarea");
                counter = cib_bar_main.querySelector('.letter-counter');
                textarea.addEventListener('input', updateLetterCounter);
                updateLetterCounter();
            } else {
                setTimeout(initLetterCounter, 100);
            }
        }
    
        document.addEventListener('DOMContentLoaded', initLetterCounter);
    })();
    

Copy

In this version of the script, the `@match` field is set to `https://www.bing.com/search*`, which means that the script will only run on URLs that start with `https://www.bing.com/search`. The rest of the script is unchanged from the previous version.

I hope this helps. Let me know if you have any further questions.

> Here is my tampermonkey script, please give some suggestions on it:
> ```
> // ==UserScript==
> // @name         Break Bing Chat Input Limit
> // @namespace    http://tampermonkey.net/
> // @version      0.1
> // @description  Break the input character limits of Bing Chat
> // @match        https://www.bing.com/search*
> // @grant        none
> // ==/UserScript==
> 
> (function() {
>     'use strict';
> 
>     let maxCount = 20000;
>     let cib_bar_main;
>     let textarea;
>     let counter;
> 
>     function updateLetterCounter() {
>         textarea.maxLength = maxCount;
>         let currentCount = textarea.value.length;
>         counter.textContent = currentCount + '/' + maxCount;
>         console.log(currentCount);
>     }
> 
>     function initLetterCounter() {
>         try {
>             cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
>             textarea = cib_bar_main.querySelector("textarea");
>             counter = cib_bar_main.querySelector('.letter-counter');
>             textarea.addEventListener('input', updateLetterCounter);
>             updateLetterCounter();
>         } catch {
>             setTimeout(initLetterCounter, 100);
>         }
>     }
> 
>     initLetterCounter();
> })();
> ```

Your Tampermonkey script looks good! It will run on URLs that start with `https://www.bing.com/search` and will update the max value of the letter counter to 20000. Here are a few suggestions to improve the script:

1.  You can remove the `console.log(currentCount);` line from the `updateLetterCounter` function as it is not necessary for the script to function and may clutter the console output.
    
2.  You can add an event listener to the `document` object to listen for the `DOMContentLoaded` event and only call the `initLetterCounter` function when the page is ready. This will ensure that the script only runs after the page has finished loading. Here’s an example:
    

    document.addEventListener('DOMContentLoaded', initLetterCounter);
    

Copy

3.  You can update the `@description` field in the script’s metadata block to provide a more detailed description of what the script does. For example:

    // @description  Breaks the input character limit of Bing Chat by increasing the max value of the letter counter to 20000
    

Copy

I hope these suggestions help improve your Tampermonkey script. Let me know if you have any further questions.

> This script has an bug that it would not update the current count when pasted text to the text area. Please fix this bug.

To fix the issue where the current count is not updated when text is pasted into the text area, you can add an additional event listener to the `textarea` element to listen for the `paste` event and update the letter counter when text is pasted. Here’s an updated version of your script that includes this fix:

    // ==UserScript==
    // @name         Break Bing Chat Input Limit
    // @namespace    http://tampermonkey.net/
    // @version      0.1
    // @description  Breaks the input character limit of Bing Chat by increasing the max value of the letter counter to 20000
    // @match        https://www.bing.com/search*
    // @grant        none
    // ==/UserScript==
    
    (function() {
        'use strict';
    
        let maxCount = 20000;
        let cib_bar_main;
        let textarea;
        let counter;
    
        function updateLetterCounter() {
            textarea.maxLength = maxCount;
            let currentCount = textarea.value.length;
            counter.textContent = currentCount + '/' + maxCount;
        }
    
        function initLetterCounter() {
            try {
                cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
                textarea = cib_bar_main.querySelector("textarea");
                counter = cib_bar_main.querySelector('.letter-counter');
                textarea.addEventListener('input', updateLetterCounter);
                textarea.addEventListener('paste', updateLetterCounter);
                updateLetterCounter();
            } catch {
                setTimeout(initLetterCounter, 100);
            }
        }
    
        initLetterCounter();
    })();
    

Copy

In this version of the script, an additional event listener is added to the `textarea` element to listen for the `paste` event. When this event is triggered, it means that text has been pasted into the text area and the `updateLetterCounter` function is called to update the letter counter. The rest of the script is unchanged from the previous version.

I hope this helps fix the issue with updating the current count when text is pasted into the text area. Let me know if you have any further questions.

> not only paste, but all updating behavior to the text area

If you want the letter counter to update for all changes to the text area, including pasting text, typing text, and other methods of updating the text area’s value, you can use the `input` event instead of the `paste` event. The `input` event is triggered whenever the value of the text area changes, regardless of how the change occurred.

Here’s an updated version of your script that uses the `input` event to update the letter counter for all changes to the text area:

    // ==UserScript==
    // @name         Break Bing Chat Input Limit
    // @namespace    http://tampermonkey.net/
    // @version      0.1
    // @description  Breaks the input character limit of Bing Chat by increasing the max value of the letter counter to 20000
    // @match        https://www.bing.com/search*
    // @grant        none
    // ==/UserScript==
    
    (function() {
        'use strict';
    
        let maxCount = 20000;
        let cib_bar_main;
        let textarea;
        let counter;
    
        function updateLetterCounter() {
            textarea.maxLength = maxCount;
            let currentCount = textarea.value.length;
            counter.textContent = currentCount + '/' + maxCount;
        }
    
        function initLetterCounter() {
            try {
                cib_bar_main = document.querySelector(".cib-serp-main").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot;
                textarea = cib_bar_main.querySelector("textarea");
                counter = cib_bar_main.querySelector('.letter-counter');
                textarea.addEventListener('input', updateLetterCounter);
                updateLetterCounter();
            } catch {
                setTimeout(initLetterCounter, 100);
            }
        }
    
        initLetterCounter();
    })();
    

Copy

In this version of the script, an event listener is added to the `textarea` element to listen for the `input` event. When this event is triggered, it means that the value of the text area has changed and the `updateLetterCounter` function is called to update the letter counter. The rest of the script is unchanged from the previous version.

I hope this helps update the letter counter for all changes to the text area. Let me know if you have any further questions.