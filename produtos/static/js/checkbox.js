function atualizarStatus(produtoId, isChecked) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;  // Pegando o CSRF token
    check()
    fetch("/atualizarProduto/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,  // CSRF token necessário para POST
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `produto_id=${produtoId}&concluida=${isChecked}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            console.log("Status atualizado com sucesso.");
        } else {
            console.error("Erro ao atualizar status:", data.message);
        }
    })
    .catch(error => {
        console.error("Erro ao atualizar status:", error);
    });
}

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
    document.addEventListener('DOMContentLoaded', () => {
        // Obtém todos os checkboxes com a classe 'item'
        const checkboxes = document.querySelectorAll(".checkbox_item");
        console.log(checkboxes);
        
        checkboxes.forEach(checkbox => {
            // console.log(checkbox.checked === true);
            if (checkbox.checked === true){
                checkbox.parentNode.parentNode.parentNode.classList.add("strikethrough")
            }
            
        });
    });
    