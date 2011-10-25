(function ($) {
    
    $(document).ready(function () {
        var ODD_CLASS = 'row2', 
            EVEN_CLASS = 'row1';

        if ($('body').is('.change-list')) {
            var orderFieldSelector = 'input[name$="-' + window.CHANGE_LIST_ORDERING_FIELD + '"]',
                updatedOrderClass = 'updated-order',
                fields = $(orderFieldSelector);
            fields.attr('readonly', true);

            $('div#changelist tbody').sortable({
                items: 'tr',
                handle: 'th:first',
                update: function () {
                    var rows = $(this).find('tr');
                    rows.each(function (i) {
                        var row = $(this),
                            field = row.find(orderFieldSelector),
                            previous = parseInt(field.val(), 10),
                            current = i + 1;
                        if (previous !== current) {
                            row.addClass(updatedOrderClass);
                            field.val(current);
                        }
                    });
                    rows.filter(':odd').addClass(ODD_CLASS).removeClass(EVEN_CLASS);
                    rows.filter(':even').addClass(EVEN_CLASS).removeClass(ODD_CLASS);
                }
            });

            window.onbeforeunload = function (event) {
                // TODO
            }
        }

        if ($('body').is('.change-form')) {
            $('.orderable').each(function (i) {
                var inline = $(this),
                    fieldSelector = 'input[name$="-' + inline.data('ordering-field') + '"]',
                    fields = inline.find(fieldSelector);

                fields.attr('readonly', true);

                if (inline.is(':has(.tabular)')) {
                    var rowSelector = 'tbody tr',
                        rows = $(rowSelector);

                    rows.not('.has_original').addClass('extra');

                    inline.delegate(rowSelector + '.extra', 'change', function (event) {
                        var row = $(this);
                        row.addClass('changed');
                    });

                    inline.find('tbody').sortable({
                        'update': function (event, ui) {
                            var rows = inline.find(rowSelector);
                            rows.filter(function (i) {
                                var row = $(this);
                                return row.is('.has_original') || row.is('.changed.extra');
                            }).each(function (i) {
                                var row = $(this),
                                    orderField = row.find(fieldSelector);
                                orderField.val(i + 1);
                            });
                            rows.filter(':even').addClass(EVEN_CLASS).removeClass(ODD_CLASS);
                            rows.filter(':odd').addClass(ODD_CLASS).removeClass(EVEN_CLASS);
                        }
                    });

                    // TODO: Consider forms without ids that have errors to be orderable rows
                    // TODO: Before submit, resort to order any new rows

                }
                else if (inline.has(':has(.stacked)')) {
                }
            })
        }

    });

//     $(document).ready(function (event) {
//         
//         if ($('body.change-list').length > 0) {
//             var orderHeader = $('thead th:contains(Order)'),
//                 orderFields = $('input[name$="-order"]'),
//                 orderCells = orderFields.closest('td');
//             
//             orderHeader.hide();
//             orderCells.hide();
//             
//             $('div#changelist tbody').sortable({
//                 items: 'tr',
//                 handle: 'th:first',
//                 update: function () {
//                     var rows = $(this).find('tr');
//                     
//                     rows.each(function (i) {
//                         var row = $(this),
//                             orderField = row.find('input[name$="-order"]'),
//                             oldValue = orderField.val(),
//                             newValue = i + 1;
//                         
//                         if (oldValue != newValue) {
//                             row.addClass('updated-order');
//                             orderField.val(i + 1);
//                         }
//                     });
//                     
//                     rows.filter(':odd').addClass('row2').removeClass('row1');
//                     rows.filter(':even').addClass('row1').removeClass('row2');
//                 }
//             });
//             
//             window.onbeforeunload = function (event) {
//                 // TODO: Make sure that explicitOriginalTarget is standard API for this event.
//                 if ($('.updated-order').length > 0 && $(event.explicitOriginalTarget).is(':not(:submit)')) {
//                     var verboseNamePlural = 'objects';
//                     if ($('#verbose-name-plural').length == 1) {
//                         verboseNamePlural = $('#verbose-name-plural').text();
//                     }
//                     return 'You have updated the order of your ' + verboseNamePlural + '.';
//                 }
//             }
//         }
//         
//         if ($('body.change-form').length > 0) {
//             $('.orderable').each(function (i) {
//                 var inline = $(this);
//                 
//                 // Tabular Inlines
//                 if (inline.is(':has(.tabular)')) {
//                     // Hide the unnecessary, ordering fields.
//                     inline.find('th:contains(Order)').hide();
//                     inline.find('td.original').hide();
//                     inline.find('input[name$="-order"]').closest('td').hide();
//                     inline.find('tbody tr.has_original').removeClass('has_original');
//                     inline.find('tbody tr').css('cursor', 'move');
//                     
//                     inline.find('tbody').sortable({
//                         'update': function (event, ui) {
//                             var rows = inline.find('tbody tr');
//                             rows.each(function (i) {
//                                 var row = $(this),
//                                     orderField = row.find('input[name$="-order"]');
//                                 orderField.val(i + 1);
//                             });
//                             rows.filter(':even').addClass('row1').removeClass('row2');
//                             rows.filter(':odd').addClass('row2').removeClass('row1');
//                         }
//                     });
//                 }
//                 // Stacked Inlines
//                 else {
//                     inline.find('.form-row.order').hide();
//                     inline.find('.inline-group h3').css('cursor', 'move');
//                     
//                     inline.find('.inline-group').sortable({
//                         'handle': 'h3',
//                         'update': function (event, ui) {
//                             var forms = inline.find('.inline-related');
//                             forms.each(function (i) {
//                                 var form = $(this),
//                                     orderField = form.find('input[name$="order"]');
//                                 orderField.val(i + 1);
//                             });
//                         }
//                     });
//                 }
//                 
//             });
//         }
//         
//     });
    
})(jQuery);
