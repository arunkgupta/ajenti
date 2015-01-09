#ajenti-plugin
from aj.api import *


info = PluginInfo(
    title='Core',
    icon='link',
    dependencies=[
    ],
    resources=[
        'resources/vendor/jquery/dist/jquery.min.js',
        'resources/vendor/angular/angular.min.js',
        'resources/vendor/angular-animate/angular-animate.min.js',
        'resources/vendor/angular-cookies/angular-cookies.min.js',
        'resources/vendor/angular-route/angular-route.min.js',
        'resources/vendor/angular-socket-io/socket.min.js',
        'resources/vendor/AngularJS-Toaster/toaster.js',
        'resources/vendor/AngularJS-Toaster/toaster.css',
        'resources/vendor/angular-loading-bar/build/loading-bar.min.js',
        'resources/vendor/angular-loading-bar/build/loading-bar.min.css',
        'resources/vendor/angular-bootstrap/ui-bootstrap-tpls.min.js',
        'resources/vendor/angular-persona/angular-persona.min.js',

        'resources/css/bootstrap/bootstrap.less',
        'resources/css/overrides.less',
        'resources/css/animations.less',
        'resources/css/app.less',
        'resources/css/responsive.less',

        'resources/js/socket.io.js',

        'resources/js/app.coffee',

        'resources/js/core/module.coffee',
        'resources/js/core/filters.coffee',
        'resources/js/core/interceptors.coffee',
        'resources/js/core/routing.coffee',
        'resources/js/core/controllers/index.controller.coffee',
        'resources/js/core/controllers/login.controller.coffee',
        'resources/js/core/controllers/root.controller.coffee',
        'resources/js/core/directives/dialog.coffee',
        'resources/js/core/directives/fitToParent.coffee',
        'resources/js/core/directives/floatingToolbar.coffee',
        'resources/js/core/directives/keyboardFocus.coffee',
        'resources/js/core/directives/ngEnter.coffee',
        'resources/js/core/directives/progressSpinner.coffee',
        'resources/js/core/directives/sidebar.coffee',
        'resources/js/core/services/hotkeys.service.coffee',
        'resources/js/core/services/identity.service.coffee',
        'resources/js/core/services/notify.service.coffee',
        'resources/js/core/services/pageTitle.service.coffee',
        'resources/js/core/services/socket.service.coffee',
        
        'resources/partial/index.html',
        'resources/partial/login.html',
        'resources/partial/sidebarItem.html',
        
        'ng:core',
        'ng:core.templates',
    ],
)


def init():
    import main
    import views.api
    import views.main
    import views.resource_server
