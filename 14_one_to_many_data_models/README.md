# Models

many to one to avoiad vertically repeations

CASCADE - when you delete a row, it also delete the rows in other table who have it as forieign key
`on_delete=models.CASCADE`

or, use set_null to make suer that won't be true
`on_delete=models.SET_NULL, null=True`