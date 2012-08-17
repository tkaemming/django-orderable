(function ($) {
    
    $(document).ready(function (event) {
        
        if ($('body.change-list').length > 0) {
            var orderHeader = $('thead th:contains(Order)'),
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
            $('.orderable').each(function (i) {
                var inline = $(this);
                
                // Tabular Inlines
                if (inline.is(':has(.tabular)')) {
                    // Hide the unnecessary, ordering fields.
                    inline.find('th:contains(Order)').hide();
                    inline.find('td.order, td.field-order').hide();
                    inline.find('tbody tr:not(.add-row)').css('cursor', 'move');
                    
                    inline.find('tbody').sortable({
                        'items': 'tr:not(.add-row)',
                        'cancel': 'tr.add-row',
                        'update': function (event, ui) {
                            var rows = inline.find('tbody tr');
                            rows.each(function (i) {
                                var row = $(this),
                                    orderField = row.find('input[name$="-order"]');
                                orderField.val(i + 1);
                            });
                            rows.filter(':even').addClass('row1').removeClass('row2');
                            rows.filter(':odd').addClass('row2').removeClass('row1');
                        }
                    }).bind('click.sortable mousedown.sortable',function(ev){
                        // Allow inputs to focus under the sortable.
                        ev.target.focus();
                        /*TODO
                        if (ev.target.tagName === "INPUT") {
                            // Disable sortable (allow dragging within input
                            // so we can edit text)
                            ev.stopPropogation();
                        }
                        */
                    });
                }
                // Stacked Inlines
                else {
                    inline.find('.form-row.order, .form-row.field-order').hide();
                    inline.find('.inline-group h3').css('cursor', 'move');
                    
                    inline.find('.inline-group').sortable({
                        'items': 'div.inline-related:not(.add-row):not(.empty-form)',
                        'cancel': 'div.add-row',
                        'handle': 'h3',
                        'update': function (event, ui) {
                            var forms = inline.find('.inline-related');
                            forms.each(function (i) {
                                var form = $(this),
                                    orderField = form.find('input[name$="order"]');
                                orderField.val(i + 1);
                            });
                        }
                    });
                }
                
            });
        }
        
    });
    
})(jQuery);
