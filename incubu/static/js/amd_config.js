!(function (root) {
    root.console || (root.console = {});
    typeof root.console.log !== 'function' && (root.console.log = function() {});

    if (typeof Function.prototype.bind === 'undefined') {
        Function.prototype.bind = function () {
            var fn = this, args = Array.prototype.slice.call(arguments), object = args.shift();
            return function () {
                return fn.apply(object,
                    args.concat(Array.prototype.slice.call(arguments)));
            };
        };
    }
    if (typeof root.addEventListener === 'undefined') {
        root.addEventListener = function (type, listener, useCapture) {
            return root.attachEvent('on' + type, listener);
        };
    }
    var require = root.require;

    require.config({
        paths: {
            jquery: 'https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min',
            underscore: 'libs/underscore/underscore-min',
            backbone: 'libs/backbone/backbone-min',
            'jquery.cookie': 'libs/jquery/jquery.cookie',
            aes: "http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/aes"
          },
        waitSeconds: 0, //15,
        shim: {
            'underscore': {
                exports: '_'
            },
            'backbone': {
                deps: ["underscore", "jquery"],
                exports: "Backbone"
            }
        }
    });

    define([
        'jquery',
        'underscore',
        'jquery.cookie'], function( $, _) {
            var startModuleName = $("script[data-main][data-start]").attr("data-start") || 'main',
                submodule = '',
                modules;
            modules = startModuleName.split('/'); // to separate submodules, like in tabs on dasboard(escritorio)
            startModuleName = modules[0];
            if (modules.length > 1) {
                submodule = _.rest(modules).join('/');
            }

            $.noConflict(), _.noConflict();

            // to start an app we need add the attribute "data-start" when we load requirejs
            // by default we load "apps/main.js".
            // for example, to start with the module /apps/dashboard.js: 
            // <script type="text/javascript" data-main="/static/js/amd_config" data-start="dashboard" src="/static/js/libs/require/require.js"></script>
            require(['apps/' + startModuleName], function (App) {
                App.initialize({submodule: submodule});
            });
    });

}(this));
