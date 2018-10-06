$(document).ready(function(){

    $('#add_more').click(function(e){
        $('#add_courses').append(
        '<div>'+
            '<input name="courses[]" id="courses" placeholder="Enter course code"/>'+
            '<input type="number" placeholder="percentage(%)" name="grades[]"/>'+
            '<input type="button" id="delete_course" value="Delete"/>'+
        '</div>');
  
    });

    $('body').on('click', '#delete_course', (function(e){
    $(this).parent('div').remove();
    }));

    

});

$(function() {
    var courses = ["coms1000", "coms1008","coms3000"];

    $('#courses').autocomplete({
        source: courses
       });
}

);
