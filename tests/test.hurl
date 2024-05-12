POST {{URL}}
HTTP 422

hurl --variable URL=http://localhost:8000/api/v1/pdf *.hurl

hurl --test --report-html build/report/ --variable URL=localhost:8080 *.hurl