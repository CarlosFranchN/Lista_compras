document.addEventListener('DOMContentLoaded', function() {
    const customSelect = document.querySelector('.custom-select');
    const header = customSelect.querySelector('.select-header');
    const optionsList = customSelect.querySelector('.options-list');
    const hiddenInput = customSelect.querySelector('input[type="hidden"]');
    
    header.addEventListener('click', function() {
        optionsList.style.display = optionsList.style.display === 'none' ? 'block' : 'none';
    });
    
    const options = customSelect.querySelectorAll('.option');
    options.forEach(option => {
        option.addEventListener('click', function() {
            const value = this.dataset.value;
            const text = this.querySelector('span').textContent;
            header.querySelector('.selected-option').textContent = text;
            hiddenInput.value = value;
            optionsList.style.display = 'none';
        });
    });
    
    document.addEventListener('click', function(e) {
        if (!customSelect.contains(e.target)) {
            optionsList.style.display = 'none';
        }
    });
});
