(function ($) {
    
    $(document).ready(function (event) {
        
        if ($('body.change-list').length > 0) {
            var orderHeader = $('th:contains(Order)'),
                orderFields = $('input[name$="-order"]'),
                orderCells = orderFields.closest('td');
            
            orderHeader.hide();
            orderCells.hide();
            
            $('div#changelist tbody').sortable({
                items: 'tr',
                handle: 'th:first',
                update: function () {
                    var rows = $(this).find('tr');
                    
                    rows.each(function (i) {
                        var row = $(this),
                            orderField = row.find('input[name$="-order"]'),
                            oldValue = orderField.val(),
                            newValue = i + 1;
                        
                        if (oldValue != newValue) {
                            row.addClass('updated-order');
                            orderField.val(i + 1);
                        }
                    });
                    
                    rows.filter(':odd').addClass('row2').removeClass('row1');
                    rows.filter(':even').addClass('row1').removeClass('row2');
                }
            });
            
            window.onbeforeunload = function (event) {
                // TODO: Make sure that explicitOriginalTarget is standard API for this event.
                if ($('.updated-order').length > 0 && $(event.explicitOriginalTarget).is(':not(:submit)')) {
                    var verboseNamePlural = 'objects';
                    if ($('#verbose-name-plural').length == 1) {
                        verboseNamePlural = $('#verbose-name-plural').text();
                    }
                    return 'You have updated the order of your ' + verboseNamePlural + '.';
                }
            }
        }
        
        if ($('body.change-form').length > 0) {
            var orderableInlines = $('.orderable');
            orderableInlines.each(function (i) {
                var orderable = $(this)
                    isTabular = orderable.is('has:(.tabular)'),
                    isStacked = orderable.is('has:(.stacked)');
                
                console.log(isTabular, isStacked);
            });
        }
        
    });
    
})(jQuery);