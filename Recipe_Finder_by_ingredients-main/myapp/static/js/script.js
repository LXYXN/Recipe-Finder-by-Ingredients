document.getElementById('ingredient-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const ingredients = document.getElementById('ingredients').value;
    fetch(`/recipes/?ingredients=${ingredients}`)
        .then(response => response.json())
        .then(data => {
            const recipeList = document.getElementById('recipe-list');
            recipeList.innerHTML = '';
            data.forEach(recipe => {
                const recipeItem = document.createElement('li');
                recipeItem.className = 'list-group-item';
                recipeItem.innerHTML = `
                    <h2>${recipe.title}</h2>
                    <img src="${recipe.image}" alt="${recipe.title}" class="img-fluid">
                    <button class="btn btn-info mt-2" onclick="fetchRecipeDetails(${recipe.id})">View Details</button>
                    <div id="details-${recipe.id}" class="mt-3" style="display: none;"></div>
                `;
                recipeList.appendChild(recipeItem);
            });
        });
});

function fetchRecipeDetails(recipeId) {
    fetch(`/recipes/${recipeId}/`)
        .then(response => response.json())
        .then(data => {
            const detailsDiv = document.getElementById(`details-${recipeId}`);
            detailsDiv.innerHTML = `
                <p>Cooking Time: ${data.readyInMinutes} minutes</p>
                <p>Instructions: ${data.instructions}</p>
                <ul>
                    ${data.extendedIngredients.map(ingredient => `<li>${ingredient.name}</li>`).join('')}
                </ul>
            `;
            detailsDiv.style.display = 'block';
        });
}
