function productCounter(){
    let span_counter = '<span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="counter" style="font-size: x-small"></span>'
    let cookies = document.cookie.split(';');
    let counter = 0;
    for (let cookie of cookies){
        if (cookie[1]==='p'){
            counter += 1
        }
    }
    $('#counter-parent').html(span_counter)
    $('#counter').html(counter)
}
function productReduceCounter(){
    let counterParent = $('#counter-parent').html()
    let productCount = $('#counter').html()
    productCount = Number(productCount)
    if (productCount > 0){
        productCount -= 1
        $('#counter').html(productCount)
    }
}
$(document).ready(function (){
    productCounter()
})