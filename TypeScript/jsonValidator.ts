type Schema = Record<string, string>;

function validateJSONAgainstSchema(json: any, schema: Schema): boolean {
  for (const key in schema) {
    if (schema.hasOwnProperty(key)) {
      const expectedType = schema[key];
      const actualType = typeof json[key];

      if (actualType !== expectedType) {
        console.error(`Validation error for key "${key}": Expected type "${expectedType}", but got "${actualType}".`);
        return false;
      }
    }
  }

  return true;
}

// Example usage
const jsonToValidate = {
  name: "John Doe",
  age: 30,
  email: "johndoe@example.com",
};

const userSchema: Schema = {
  name: "string",
  age: "number",
  email: "string",
};

const isValid = validateJSONAgainstSchema(jsonToValidate, userSchema);
if (isValid) {
  console.log("JSON is valid according to the schema.");
} else {
  console.error("JSON is not valid according to the schema.");
}
