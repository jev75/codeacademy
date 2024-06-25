// mysite/static/js/my_custom_setup.js

function my_custom_setup(editor) {
    editor.ui.registry.addButton('copytoclipboard', {
        text: 'Copy to Clipboard',
        onAction: function () {
            copyToClipboard();
        },
        classes: 'my-custom-button' // Add this line
    });
}