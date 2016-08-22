// Copyright (c) 2016, Africlouds Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('MQTT Client', {
	refresh: function(frm) {

	},
	start: function(frm, cdt, cdn) {
		var client = frappe.model.get_doc(cdt, cdn);	
		frappe.call({
			method: "mqtt.mqtt.doctype.mqtt_client.mqtt_client.start_mqtt",
			args: {
				ip: client.ip,
				port: client.port
			}
		});
	}
});
