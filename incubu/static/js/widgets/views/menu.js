define(['backbone', 'jquery', 'underscore'], function (BB, $, _) {
    return BB.View.extend({
        initialize: function () {
        },

        render: function () {
            $('.nav li').hover(
              function () { //appearing on hover
                $('ul', this).fadeIn();
              },
              function () { //disappearing on hover
                $('ul', this).fadeOut();
              }
            );
        }
    });
});
