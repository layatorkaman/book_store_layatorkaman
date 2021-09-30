
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var bookId = this.dataset.book
		var action = this.dataset.action
		console.log('bookId:', bookId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(bookId, action)
		}else{
			updateUserOrder(bookId, action)
		}
	});
}

function updateUserOrder(bookId, action){
  console.log('User is authenticated, sending data...')
	if( action=="add") {
		var url = 'update_item/'

	}
	else if (action == "remove"){

		var url=" http://127.0.0.1:8000/store/update_item/"
	}



 fetch(url ,{
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        // 'X-CSRFToken':csrftoken,
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body:JSON.stringify({'bookId':bookId, 'action':action})

    })
    .then((response) => {
       return response.json();
    })
    .then((data) => {
      // location.reload()
      console.log('testttt')
    });
}



function addCookieItem(bookId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[bookId] == undefined){
		cart[bookId] = {'quantity':1}

		}else{
			cart[bookId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[bookId]['quantity'] -= 1

		if (cart[bookId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[bookId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	// location.reload()
};


