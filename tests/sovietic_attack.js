// NOTE: This test is not covered by pytest(what a surprise (◕⌓◕) ), it just performs
// massive requests to the application in order to test it's
// performance. Please, do not forget to just run it with the application running.
// Instal k6 to run this test with: https://k6.io/docs/getting-started/installation/
// run the thest with `k6 run sovietic_attack.js`
import http from 'k6/http';

export const options = {
  insecureSkipTLSVerify: true,

  scenarios: {
    constant_request_rate: {
      executor: 'constant-arrival-rate',
      rate: 1000,
      timeUnit: '1s',
      duration: '1s',
      preAllocatedVUs: 100,
      maxVUs: 200,
    },
  },
};

export default function () {
  http.get('https://127.0.0.1:5000/currency/?currency_id=USD');
  // http.get(
  //   'https://127.0.0.1:5000/currency_converter/?from_currency=USD&to_currency=BRL&amount=10000000'
  // );
  // http.get('https://127.0.0.1:5000/currencies/?page_size=1&page_number=1');
}
