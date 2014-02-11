'use strict'

angular.module('yeomanSampleApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
])
  .config ($routeProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when "/go",
        templateUrl: 'views/main.html'
        controller: "SearchCntrl"
      .when "/about",
        templateUrl: 'views/about_scroll.html'
        controller: 'MainCtrl'
      .when "/contact",
        templateUrl: 'views/contact.html'
        controller: 'MainCtrl'
      .otherwise
        redirectTo: '/'
