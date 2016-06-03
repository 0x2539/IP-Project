(function(){
    
    function globalController(){
        var vm = this;
        
        vm.loggedIn = false;
        vm.userName = "Sorin";
    }
    
    angular.module("mainApp")
        .controller("globalController", globalController);
})();