/**
 * This simple script simply handles toggling our "edit mode" on the front end.
 * Since our backend just accepts form POST requests as expected, 
 * we don't need any complex logic - just showing and hiding the correct HTML elements!
 */

function toggleEditMode(taskId) {
    // Find our elements
    const editFormContainer = document.getElementById(`edit-form-${taskId}`);
    const displayContainer = document.getElementById(`display-${taskId}`);

    // If edit form is currently hidden, we should show it
    if (editFormContainer.classList.contains('hidden')) {
        // 1. Unhide the form by removing the "hidden" CSS utility class
        editFormContainer.classList.remove('hidden');
        
        // 2. Temporarily hide the display text & action buttons
        displayContainer.style.display = 'none';
        
        // 3. Convenience: Automatically focus the input for the user
        const inputToFocus = editFormContainer.querySelector('input[type="text"]');
        if (inputToFocus) {
            inputToFocus.focus();
            
            // Move cursor to the end of the input's current text
            const currentValue = inputToFocus.value;
            inputToFocus.value = '';
            inputToFocus.value = currentValue;
        }
    } else {
        // If it's already shown, hide it (the user clicked "Cancel")
        editFormContainer.classList.add('hidden');
        
        // Return the display text to being a flexbox (its normal layout state)
        displayContainer.style.display = 'flex';
    }
}
