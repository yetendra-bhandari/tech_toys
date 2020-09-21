import moment from "moment";
const helper = {
    computed: {
        serverURL() {
            return process.env.VUE_APP_SERVER_URL;
        },
    },
    methods: {
        dateTimeFormat(datetime) {
            return moment(datetime).format("h:mma, DD MMMM, YYYY");
        },
        truncateAddress(address, maxLength) {
            let locality =
                address.locality.length > maxLength ?
                address.locality.slice(0, maxLength) + "..." :
                address.locality;
            let city =
                address.city.length > maxLength ?
                address.city.slice(0, maxLength) + "..." :
                address.city;
            let state =
                address.state.length > maxLength ?
                address.state.slice(0, maxLength) + "..." :
                address.state;
            return locality + ", " + city + ", " + state + " - " + address.pincode;
        },
    }
}
export default helper