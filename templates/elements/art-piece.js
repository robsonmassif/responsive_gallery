(function(){
Polymer({
  is: 'art-piece',
  properties: {
    label: {
      type: String
    },
    art: {
      type: Number
    }
  },
  ready: function() {
    console.log("Art Piece ready", this.label);
  }
});
})();
