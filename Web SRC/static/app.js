var app = angular.module('plantApp', [ ]);

app.controller('PlantController', ['$scope', function($scope) {
	$scope.yourname = '';
	$scope.change = function() {
		$scope.yourname = 'static/img.jpg';
	};
}]);