(function(){
Polymer({
  is: 'art-piece',
  properties: {
    label: {
      type: String
    }
  },
  ready: function() {
    console.log("Art Piece ready", this.label);
  }
});
})();
