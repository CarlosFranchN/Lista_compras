function check() {
    // Obtém todos os checkboxes com a classe 'item'
    const checkbox = document.querySelector(".checkbox_item");
    const pai = checkbox.parentNode.parentNode.parentNode
    console.log(checkbox);
    console.log(pai);
      if (checkbox.checked) {
        // Adiciona a classe 'strikethrough' ao nome do item e à caixa
        pai.classList.add("strikethrough");
      } else {
        // Remove a classe 'strikethrough' se o checkbox for desmarcado
        pai.classList.remove("strikethrough");
      }

    }
