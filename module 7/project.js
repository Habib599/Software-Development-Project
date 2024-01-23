const loaddata = () => {
    const searchText = document.getElementById("search-box").Value;
    console.log(searchText);
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText}`)
        .then((res) => res.json())
        .then((data) => displayData(data.meals));
};
const displayData = (data) =>{
    document.getElementById("total-meals").innerText=data.length;

    const mealscontainer=document.getElementById("meals-container");

    data.forEach(meal => {
        console.log(meal);
        const card= document.createElement("div");
        card.classList.add("box");
        card.innerHTML=`
        <img class="box-img" src=${meal.strMealThumb} alt="">
        <h2>${meal.strmeal}</h2>
        <p>${meal.strInstruction.slice(0,50)}</p>
        <button>Details</button>
        `;
        mealscontainer.appendChild(card);
    });
};