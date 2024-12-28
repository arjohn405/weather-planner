import React, { useState } from 'react';
import {
  ChakraProvider,
  Box,
  VStack,
  Grid,
  theme,
  Container,
  Heading,
  FormControl,
  FormLabel,
  Input,
  NumberInput,
  NumberInputField,
  Button,
  Text,
  useToast,
  Card,
  CardBody,
  Divider,
} from '@chakra-ui/react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    activity: '',
    dateTime: '',
    peopleCount: 1,
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const toast = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/api/plan-activity', formData);
      setResult(response.data);
    } catch (error) {
      toast({
        title: 'Error',
        description: 'Failed to get recommendations. Please try again.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }

    setLoading(false);
  };

  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl" p={5}>
        <Container maxW="container.md">
          <VStack spacing={8}>
            <Heading as="h1" size="xl" colorScheme="teal">
              Activity Planner
            </Heading>

            <Card width="100%" p={5}>
              <CardBody>
                <form onSubmit={handleSubmit}>
                  <VStack spacing={4}>
                    <FormControl isRequired>
                      <FormLabel>What activity would you like to do?</FormLabel>
                      <Input
                        placeholder="e.g., hiking, dining, shopping"
                        value={formData.activity}
                        onChange={(e) =>
                          setFormData({ ...formData, activity: e.target.value })
                        }
                      />
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel>When would you like to do this?</FormLabel>
                      <Input
                        type="datetime-local"
                        value={formData.dateTime}
                        onChange={(e) =>
                          setFormData({ ...formData, dateTime: e.target.value })
                        }
                      />
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel>Number of people</FormLabel>
                      <NumberInput
                        min={1}
                        value={formData.peopleCount}
                        onChange={(value) =>
                          setFormData({ ...formData, peopleCount: parseInt(value) })
                        }
                      >
                        <NumberInputField />
                      </NumberInput>
                    </FormControl>

                    <Button
                      width="100%"
                      colorScheme="teal"
                      type="submit"
                      isLoading={loading}
                    >
                      Get Recommendations
                    </Button>
                  </VStack>
                </form>
              </CardBody>
            </Card>

            {result && (
              <Card width="100%" p={5}>
                <CardBody>
                  <VStack spacing={4} align="stretch">
                    <Heading size="md">Weather Forecast</Heading>
                    <Grid templateColumns="repeat(3, 1fr)" gap={4}>
                      <Box>
                        <Text fontWeight="bold">Temperature</Text>
                        <Text>{result.weather.temperature}°C</Text>
                      </Box>
                      <Box>
                        <Text fontWeight="bold">Conditions</Text>
                        <Text>{result.weather.conditions}</Text>
                      </Box>
                      <Box>
                        <Text fontWeight="bold">Humidity</Text>
                        <Text>{result.weather.humidity}%</Text>
                      </Box>
                    </Grid>

                    <Divider />

                    <Box>
                      <Heading size="md">Recommendation</Heading>
                      <Text whiteSpace="pre-line" mt={2}>
                        {result.recommendation}
                      </Text>
                    </Box>
                  </VStack>
                </CardBody>
              </Card>
            )}
          </VStack>
        </Container>
      </Box>
    </ChakraProvider>
  );
}

export default App; 