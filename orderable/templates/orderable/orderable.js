/*
    
    Django Administration Ordering
    by Ted Kaemming <ted@kaemming.com>
    
    Requires jQuery and jQuery UI.
    
*/

$(document).ready(function (event) {
    
    $('div#changelist tbody').sortable({
        items: 'tr',
        handle: 'th:first',
        update: function() {
            var parameters = {
                    'app_label': Orderable.app_label,
                    'model_name': Orderable.model_name,
                },
                rows = $(this).find('tr');
                
            rows.each(function (i) {
                var orderField = $(this).find('input.ordering');
                orderField.val(i + 1);
                parameters[orderField.attr('name')] = orderField.val();
            });
            
            $.post('{% url orderable_order_objects %}', parameters);
            
            rows.each(function (i) {
                var row = $(this);
                row.removeClass('row1').removeClass('row2');
                if (i % 2 == 0) {
                    row.addClass('row1');
                }
                else {
                    row.addClass('row2');
                }
            });
        }
    });
    
    $('div#changelist tbody th:first').css('cursor', 'move');
    $('div#changelist thead tr th:last').hide();
    $('div#changelist tbody').find('input.ordering').parent('td').hide();
    
});