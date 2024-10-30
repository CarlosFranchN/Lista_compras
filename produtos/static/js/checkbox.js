function atualizarStatus(produtoId, isChecked) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;  // Pegando o CSRF token

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
