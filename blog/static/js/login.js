$(document).ready(function(){
    $('.btn-primary').click(function(){
        $.ajax({
            url : `http://127.0.0.1:8000/token/`,
            method: 'POST',
            data : {username : $('#loginform').val(),
                    password : $('#passform').val()}
          }).done(function(msg){
            console.log(msg)
            localStorage.setItem('access_token', msg.access)
            document.location.href = 'http://127.0.0.1:8000/home'
          })
          .fail(function(){
            alert('Не правильный логин или пароль попробуйте еще раз!');
            document.location.href = 'http://127.0.0.1:8000/login?  '
          });
          
          $.ajax({
            url : `http://127.0.0.1:8000/courier/get/`,
            method: 'GET',
            headers: {'Authorization' : `Bearer ${localStorage.getItem('access_token')}`}
          }).done(function(msg){
            console.log(msg);
          })
          .fail(function(){
            console.log('Кто ты воин?')
          })
    })
})