    function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#blah')
                        .attr('src', e.target.result)
                        .width(150)
                        .height(200)
                        ;
                         var button= document.createElement("button"); 
                        button.innerHTML = "Recommend";
                        button.id='recommendButton';
                        if(!document.getElementById('recommendButton')){
                        $("#recommend").append(button); }

                };

                reader.readAsDataURL(input.files[0]);
            }
        }