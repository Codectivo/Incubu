define(function (require, exports, module) {
    var $ = require('jquery'),
        _ = require('underscore'),
        BB = require('backbone'),
        Menu = require('widgets/views/menu'),

        View = BB.View.extend({
        initialize: function (options) {
            this.options = options || {};
        },

        activatePage: function (submodule) {
            var view = this;
            this._activeTab instanceof BB.View && this._activeTab.remove();
            require(['widgets/views/' + submodule], function (TabView) 
                {
                    view._activeTab = new TabView(view.options);
                    view._activeTab.on('all', function () {
                       this.trigger.apply(view, arguments);
                    }, view);
                });
        },

        render: function (site) {
            new Menu().render();
            this.options.submodule && this.activatePage(this.options.submodule);
        }
    });
    BB = BB.noConflict();

    return {
        initialize: function (params) {
            new View(params || {}).render();
        }
    };
});