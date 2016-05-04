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
    dialog = this.$.testDialog;
    dialog.open();
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
  },

  submitForm: function() {
    that = this;
    new_art = this.$.newArt.value;
    new_label = this.$.newLabel.value;
    console.log(new_art, new_label);
    gapi.client.gallery.new.composition({'art': new_art, 'label': new_label}).execute(
      function(resp) {
        if (!resp.code) {
            that.push('collection', {name: resp.label, num: resp.art});
            that.$.testDialog.close();
        }
      });
  }
});
})();
