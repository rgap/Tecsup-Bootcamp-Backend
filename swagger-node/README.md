## OpenAPI/Swagger Specification

**Swagger:** Framework that uses the OpenAPI/Swagger Specification, which is a standard way of describing RESTful APIs.

OpenAPI specification defines a set of rules in YAML or JSON format for describing the structure of an API, including endpoints, parameters, request and response payloads, authentication methods, ...

## Example in json

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Sample API",
    "version": "1.0.0"
  },
  "paths": {
    "/hello": {
      "get": {
        "summary": "Returns a greeting message",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
