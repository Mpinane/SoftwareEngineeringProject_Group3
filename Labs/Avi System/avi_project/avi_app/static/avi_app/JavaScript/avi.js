$(document).ready(function(){

    $('#add_more').click(function(e){
        $('#add_courses').append(
        '<div>'+
            '<select>'+
                '{% for i in courses %}'+
                    '<option name="courses[]" value="{{i}}">{{i}}<option/>'+
                '{% endfor %}'+
            '</select>'+
            '<input type="number" placeholder="percentage(%)" name="grades[]"/>'+
            '<input type="button" id="delete_course" value="Delete"/>'+
        '</div>');
  
    });

    $('body').on('click', '#delete_course', (function(e){
    $(this).parent('div').remove();
    }));

});
