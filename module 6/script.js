

function setInnerText  (id, value){
    document.getElementById(id).innerText= value;
}

function handleDeposit()
{
    const inputValue = parseInt(document.getElementById("deposit-input").value)
    const depositeAmount=parseInt( document.getElementById("deposit-amount").innerText);
    const sum = inputValue + depositeAmount;

    setInnerText("deposit-amount", sum)
    // document.getElementById("deposit-amount").innerText= sum;
    const totaAlmount=parseInt(document.getElementById("total-amount").innerText);
    const totalsum=inputValue +totaAlmount;
    setInnerText("total-amount", totalsum)
    // document.getElementById("total-amount").innerText=totalsum;
    // document.getElementById("deposit-input").value=""

}


function handleWithdraw()
{
    const inputValue = parseInt(document.getElementById("withdraw-input").value)
    const withdrawamount=parseInt(document.getElementById("withdraw-amount").innerText);
    const sum = inputValue + withdrawamount;

    setInnerText("withdraw-amount", sum)
    // document.getElementById("withdraw-amount").innerText=sum;
    const totaAlmount=parseInt(document.getElementById("total-amount").innerText);
    const totalsum=totaAlmount - inputValue;

    setInnerText("total-amount", totalsum)
    // document.getElementById("total-amount").innerText= totalsum;
    // document.getElementById("withdraw-input").value= "";
}