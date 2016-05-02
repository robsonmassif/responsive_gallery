(function(){
Polymer({
  is: 'test-app',
  properties: {
    appliedLabel: {
      type: String
    }
  },
  ready: function() {
    this.appliedLabel = "testerati";
    this.collection = [];
    console.log("ready, ", Polymer.version, this.collection);
  },

  openDialog: function() {
    this.appliedLabel = "Changed";
    content = this.$.apiContent;
    dialog = this.$.testDialog;
    gapi.client.gallery.messages.sayHello().execute(
      function(resp) {
        if (!resp.code) {
          console.log("response: ", resp);
          content.innerText = resp.label;
          dialog.open();
        }
      });
  },

  getLabels: function() {
    that = this;
    gapi.client.gallery.fill.labels().execute(
      function(resp) {
        if (!resp.code) {
          resp.items = resp.items || [];
          for (var i = 0; i < resp.items.length; i++) {
            that.push('collection', {name: resp.items[i].label, num: resp.items[i].art});
          }
        }
      });
  }
});
})();
